var map;
function initMap() {
    // latitude and longitude vars are defined in map.html, so that
    // the vars from the view function can be used
    map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: latitude, lng: longitude },
      zoom: 10
    });
}