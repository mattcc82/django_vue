<template>
  <v-app id="mainApp" dark>
    <v-navigation-drawer
      v-model="drawer"
      clipped
      fixed
      app
    >
      <v-list dense>
        <v-list-tile exact :to="{ name: 'home' }" >
          <v-list-tile-action>
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile exact :to="{ name: 'home' }">
          <v-list-tile-action>
            <v-icon>comment</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Ask Question</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile exact href="/accounts/logout/">
          <v-list-tile-action>
            <v-icon>exit_to_app</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Log Out</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app fixed clipped-left>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>
        <router-link exact :to="{ name: 'home' }">QandA</router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" icon flat exact :to="{ name: 'home' }">
              <v-icon>home</v-icon>
            </v-btn>
          </template>
          <span>Home</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" icon flat exact :to="{ name: 'home' }">
              <v-icon>comment</v-icon>
            </v-btn>
          </template>
          <span>Ask Question</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" icon flat exact href="/accounts/logout/">
              <v-icon>exit_to_app</v-icon>
            </v-btn>
          </template>
          <span>Log Out</span>
        </v-tooltip>
      </v-toolbar-items>
    </v-toolbar>
    <v-content>
      <v-container fluid fill-height>
        <v-layout>
          <v-flex>
            <transition name="fade" mode="out-in">
              <router-view></router-view>
            </transition>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-footer app fixed>
      <span>QandA</span>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      drawer: null
    }
  }
}
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.v-toolbar__title > a {
  text-decoration: none;
  color: #fff;
}
</style>
