<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">{{ gameserver.info.server_name }}</p>
    </header>
    <div class="card-image">
      <figure class="image is-2by1">
        <a href="{% url 'gameserver_detail' pk=gameserver.pk %}">
          {% comment %}
          <img
            src="https://static.wikia.nocookie.net/cswikia/images/1/1e/CSGO_Mirage_latest_version.jpg/revision/latest/scale-to-width-down/350?cb=20200301201524"
          />
          {% endcomment %}
          <img
            src="{{ gameserver.map_image }}"
            alt="{{ gameserver.map_image }}"
          />
        </a>
      </figure>
    </div>
    <div class="card-content">
      <div class="columns">
        <div class="column">
          <ul>
            <li>
              <span class="icon">
                <i class="mdi mdi-map-marker"></i>
              </span>
              {{ gameserver.info.map_name }}
            </li>
            <li>
              <span class="icon">
                <i class="mdi mdi-account-multiple"></i>
              </span>
              {{ gameserver.info.player_count }} /
              {{ gameserver.info.max_players }}
            </li>
          </ul>
        </div>
        <div class="column">
          <ul>
            <li>
              <span class="icon">
                <i
                  class="mdi mdi-lock {% if gameserver.info.password_protected %} has-text-danger {% else %} has-text-success {% endif %}"
                ></i>
              </span>
              {% if gameserver.info.password_protected %} Password:
              <code>{{ gameserver.player_password }}</code>
              {% else %} No Password {% endif %}
            </li>
            <li>
              <span class="icon">
                <i
                  class="mdi mdi-police-badge {% if gameserver.info.vac_enabled %} has-text-success{% endif %}"
                ></i>
              </span>
              {% if gameserver.info.vac_enabled %} VAC Enabled {% else %} VAC
              Disabled {% endif %}
            </li>
            <li>{{ gameserver.test }}</li>
          </ul>
        </div>
      </div>
    </div>
    <footer class="card-footer">
      <a
        href="steam://connect/{{ gameserver.url }}:{{ gameserver.port }}"
        class="card-footer-item"
        >Join Server</a
      >
      <a href="#" class="card-footer-item">Watch GOTV</a>
      <a
        href="{% url 'gameserver_detail' pk=gameserver.pk %}"
        class="card-footer-item"
        >View Details</a
      >
    </footer>
  </div>
</template>

<script>
import { ref, computed } from "vue";

setup(){
    const gameservers = ref();
}
</script>
