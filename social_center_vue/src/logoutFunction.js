export default {
  install(Vue, options) {
    Vue.mixin({
      methods: {
        logOut() {
          // console.log('hello');
            localStorage.clear();
            $.ajaxSetup({
              headers: {'Authorization': null}
            });
            this.$router.push('/login')
        }
      }
    })
  }
};
