<template>
  <div
    class="w-48 bg-navbar-primary min-h-screen border border-black border-100 float-left px-5 pt-5"
  >
    <div class="tabs">
      <div
        class="tab"
        :class="{ active: activeTab === 'tab1' }"
        @click="changeTab('tab1')"
      >
        Tab 1
      </div>
      <div
        class="tab"
        :class="{ active: activeTab === 'tab2' }"
        @click="changeTab('tab2')"
      >
        Tab 2
      </div>
    </div>
    <div class="content">
      <div v-if="activeTab === 'tab1'">
        <!-- Content for Tab 1 -->
        <p>This is the content of Tab 1.</p>
      </div>
      <div v-if="activeTab === 'tab2'">
        <!-- Content for Tab 2 -->
        <p>This is the content of Tab 2.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: "tab1", // Default active tab
    };
  },
  methods: {
    changeTab(tabName) {
      this.activeTab = tabName;
    },
  },
};
</script>

<style>
.sidebar {
  width: 250px;
  background-color: #333;
  color: white;
  padding: 20px;
}

.tabs {
  display: flex;
}

.tab {
  cursor: pointer;
  padding: 10px;
  transition: background-color 0.2s;
  border-right: 1px solid #555; /* Add a separator between tabs */
}

.tab:last-child {
  border-right: none; /* Remove separator for the last tab */
}

.tab:hover {
  background-color: #555;
}

.content {
  margin-top: 20px;
}
</style>
