var app = new Vue({
  el: "#app",
  data: {
    win_size: null,
    x: 0,
    y: 0
  },
  created() { },
  mounted() {
    this.sizedCanvas();
  },
  updated() {

  },
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

    },
    updateCanvas: function () {
      var t = document.getElementById("i_canvas");
      var ctx = t.getContext("2d");
      var img = new Image();
      img.onload = function () {
        ctx.drawImage(img, 0, 0);
      };
      img.src = "/img?t=" + Date.parse(new Date());
    },
    onMove: function (e) {
      this.x = e.offsetX;
      this.y = e.offsetY;
    },
    onClick: function () {
      axios.get("/win/click", {
        params: {
          x: this.x,
          y: this.y
        }
      }).then((response) => { this.updateCanvas() })
    }
  },
  delimiters: ["[[", "]]"],
});
