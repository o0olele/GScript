var app = new Vue({
  el: "#app",
  data: {
    winlist: null,
  },
  created() {
    axios
      .get("/win/list")
      .then((response) => (this.winlist = response.data.data.windows))
      .catch(function (error) {
        console.log(error);
      });
  },
  delimiters: ["[[", "]]"],
});
