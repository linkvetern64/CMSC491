
// This example requires the Visualization library. Include the libraries=visualization
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=visualization">

var map, heatmap, paused = true, timing = 3000, points = [];

/**
 * Default map is set to Baltimore
 */
function initMap() {

    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: {lat: 39.283, lng: -76.612},
        mapTypeId: 'satellite'
    });

     heatmap = new google.maps.visualization.HeatmapLayer({
        map: map
        });

    // Fetch the data points
    fetchPoints()

}

function toggleHeatmap() {
    heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient() {
    var gradient = [
        'rgba(0, 255, 255, 0)',
        'rgba(0, 255, 255, 1)',
        'rgba(0, 191, 255, 1)',
        'rgba(0, 127, 255, 1)',
        'rgba(0, 63, 255, 1)',
        'rgba(0, 0, 255, 1)',
        'rgba(0, 0, 223, 1)',
        'rgba(0, 0, 191, 1)',
        'rgba(0, 0, 159, 1)',
        'rgba(0, 0, 127, 1)',
        'rgba(63, 0, 91, 1)',
        'rgba(127, 0, 63, 1)',
        'rgba(191, 0, 31, 1)',
        'rgba(255, 0, 0, 1)'
    ]
    heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
}

function changeRadius() {
    heatmap.set('radius', heatmap.get('radius') ? null : 20);
}

function changeOpacity() {
    heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
}

// Heatmap data: 500 Points
function getPoints() {
    return [
        new google.maps.LatLng(39.282525, -76.612489),
        new google.maps.LatLng(39.282425, -76.612289),
        new google.maps.LatLng(39.283525, -76.612189),
        new google.maps.LatLng(39.282525, -76.612389),
        new google.maps.LatLng(39.282515, -76.612589),
        new google.maps.LatLng(39.282535, -76.612189),
        new google.maps.LatLng(39.282545, -76.612189),

    ];
}

function fetchPoints() {
    return fetch('lat-long-data.json')
      .then(body => body.json())
      .then(({ data }) => data.map(({ latitude, longitude }) =>
        new google.maps.LatLng(latitude, longitude),
      ))
      .then(newPoints => {
        points.push(newPoints)
      })
      .catch(err => console.error(err))
}

function populatePoints(index){
    //This file will read the crime data and create an array of lat-lng points
    //
    points.push([
        new google.maps.LatLng(39.283525, -76.616489),
        new google.maps.LatLng(39.283425, -76.611289),
        new google.maps.LatLng(39.283525, -76.612189),
        new google.maps.LatLng(39.283525, -76.610389),
        new google.maps.LatLng(39.283515, -76.613589),
        new google.maps.LatLng(39.283535, -76.611189),
        new google.maps.LatLng(39.283545, -76.614189),
      ])

    return points[index]
}

function playMap(){
    paused = false;
    var i = 0;
    numPoints = 2

    // Initialize a heat map
    heatmap = new google.maps.visualization.HeatmapLayer({
      data: populatePoints(0),
      map,
    });

    setInterval(function(){
        if(!paused){
        heatmap.setData([])

        //Keep index within bounds of point array
        i = (i + 1) % numPoints

        //Generate new heatmap with visualization
        heatmap = new google.maps.visualization.HeatmapLayer({
        data: populatePoints(i),
        map: map
        });

        }
    }, timing);
}

function pauseMap(){
    paused = true;
}
