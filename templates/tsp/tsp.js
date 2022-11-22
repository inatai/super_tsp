var dist_data = [];
var name;
var marker=null;
var lat = 35.729493379635535;
var lng = 139.71086479574538;
dist_count = 0;//インデックスの初期化
const dist_data2 = [];

function init() {
//初期化
var map = new google.maps.Map(document.getElementById('map'), {
zoom: 18,
center: {
  lat: lat,
  lng: lng
}
});
console.log("ここまでは成功");
/*marker = new google.maps.Marker({
  map: map, positon: new google.maps.latLng(lat, lng),
});*/

//クリックイベント
map.addListener('click', function(e) {
  map.panTo(e.latLng);  
  clickMap(e.latLng);
});
}


function clickMap(latlng) {
  var geocoder = new google.maps.Geocoder();

  geocoder.geocode(
    {latLng: latlng},
    function(results, status)
    {
      if(status == google.maps.GeocoderStatus.OK){
        if($('div').hasClass('title')){
          //titleというクラスが存在する時の処理
          const results = document.getElementsByClassName('title');
          console.log(results[0]);
          dist_data2.push({
            address: results[0].innerText,
            lat: latlng.lat(),
            lng: latlng.lng()
          });
        }
        else if(results[0].geometry){
          var address = results[0].formatted_address;
          dist_data2.push({
            address: address,
            lat: latlng.lat(),
            lng: latlng.lng()
          });
        }
      }
      else{
        dist_data2.push({
          address: "address",
          lat: latlng.lat(),
          lng: latlng.lng()
        });
      }
      console.log(dist_data2);
      
      marker.setMap(null);
      marker = null;
      marker = new google.maps.Marker({ 
        position: latlng,
        map: map
      });
   })
  }  

function clickBtn() {
  $.ajax({
    url: "{% url 'tsp:call_write_data' %}",
    method: 'GET',
    data: JSON.stringify(dist_data2),
    dataType: "json",
    contentType: "application/json",
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrf_token);
      }
    },
    error: function(xhr, status, error) {
      console.log("error")
    }
  })
  .done(function(data) {
    console.log("Success"); 
  });

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  // ヘッダにcsrf_tokenを付与する関数
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  };
}
</script>