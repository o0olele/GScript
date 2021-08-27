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
  methods: {
    onLive: function () {
      var winName = $("#i_win").val();

      if (winName.length <= 0) {
        console.log("please choose window first!");
        return;
      }

      axios
        .get("/win/init", {
          params: {
            win: winName,
          },
        })
        .then(function (response) {
          var ret = response.data;

          if (ret.errcode != 0) {
            return
          }

          window.location.href = "/live";
        });
    },
  },
  delimiters: ["[[", "]]"],
});
