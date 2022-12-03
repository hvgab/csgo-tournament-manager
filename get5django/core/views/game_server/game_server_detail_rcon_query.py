from django.views.generic import DetailView
from django.views.generic.edit import FormView, FormMixin
from django.views.generic.detail import SingleObjectMixin

from core.models import GameServer
from core.services.a2s_service import A2sService
from core.services.a2s_info_service import A2sInfoService
from core.services.og_image_service import OgImageService
from core.services.rcon_service import RconService

from core.forms.game_server_rcon_query import RconQueryForm
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

class GameServerDetailRconQueryView(FormView, SingleObjectMixin):
    model = GameServer
    template_name = "game_server/game_server_detail_rcon_query.html"
    form_class = RconQueryForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


    def get_context_data(self, **kwargs):
        logger.debug('Start: Get Context Data')
        context = super().get_context_data(**kwargs)

        logger.debug(context['gameserver'])
        gameserver = context["gameserver"]

        logger.debug(self.request.POST)

        if 'rcon_response' in kwargs:
            context['rcon_response'] = kwargs.get('rcon_response')

        info = A2sInfoService.execute({'address':f'{gameserver.url}:{gameserver.port}'})
        context['info'] = info
        context["a2s"] = A2sService.execute({'game_server': gameserver})
        map_name = info['map_name']
        if "/" in map_name:
            map_name = map_name.split('/')[1]
            logger.debug(map_name)
        context[f"{info['server_name']}_image"] = OgImageService.execute({'url':f'https://steamcommunity.com/sharedfiles/filedetails/?id={map_name}'})
        logger.debug('End: Get Context Data')
        return context
    
    def form_valid(self, request, *args, **kwargs):
        logger.debug('args: ')
        logger.debug(args)
        logger.debug('kwargs: ')
        logger.debug(kwargs)

        form = self.form_class(self.request.POST)
        logger.debug('form')
        logger.debug(form)
        
        self.object = self.get_object()
        logger.debug('self.object')
        logger.debug(self.object)

        context = self.get_context_data(object=self.object)
        logger.debug('context')
        logger.debug(context)
        
        logger.debug('cleaned data')
        logger.debug(form.cleaned_data)
        
        cd = form.cleaned_data
        logger.debug(cd)

        rcon_response = None

        logger.debug('rcon service vars')
        logger.debug(f"{context['gameserver']=}")
        logger.debug(f"{cd['query']=}")

        gameserver = context['gameserver']
        command = cd['query']
        logger.debug('rcon service vars')
        logger.debug(f"{gameserver=}")
        logger.debug(f"{command=}")

        rcon_response = RconService.execute(
            {
                'gameserver':gameserver, 
                'command': command,
            }
        )
        
        logger.debug('rcon response')
        logger.debug(rcon_response)

        context['rcon_response'] = rcon_response

        # return self.get(rcon_response=rcon_response)
        return self.render_to_response(context)

    