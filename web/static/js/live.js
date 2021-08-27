var app = new Vue({
  el: "#app",
  data: {
    win_size: null,
  },
  created() {},
  mounted() {},
  watch: {},
  methods: {
    sizedCanvas: function () {
      axios.get("/win/size").then(function (response) {
        this.win_size = response.data.data;

        if (this.win_size.length != 4) {
          return;
        }
        $("#i_canvas").attr("width", this.win_size[2] - this.win_size[0]);
        $("#i_canvas").attr("height", this.win_size[3] - this.win_size[1]);
      });
      this.updateCanvas();
    },
    updateCanvas: function () {
      var t = document.getElementById("i_canvas");
      var ctx = t.getContext("2d");
      var img = new Image();
      img.onload = function () {
        ctx.drawImage(img, 0, 0);
      };
      img.src = "/img";
    },
  },
  delimiters: ["[[", "]]"],
});
