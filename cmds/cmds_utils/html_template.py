__author__ = "Daniele Capocefalo, Mauro Truglio, Tommaso Mazza"
__copyright__ = "Copyright 2018, The Pyntacle Project"
__credits__ = ["Ferenc Jordan"]
__version__ = "0.2.4"
__maintainer__ = "Daniele Capocefalo"
__email__ = "d.capocefalo@css-mendel.it"
__status__ = "Development"
__date__ = "27 February 2018"
__license__ = u"""
  Copyright (C) 2016-2018  Tommaso Mazza <t,mazza@css-mendel.it>
  Viale Regina Margherita 261, 00198 Rome, Italy

  This program is free software; you can use and redistribute it under
  the terms of the BY-NC-ND license as published by
  Creative Commons; either version 4 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  License for more details.

  You should have received a copy of the license along with this
  work. If not, see http://creativecommons.org/licenses/by-nc-nd/4.0/.
  """

html_template = u"""




<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Herald</title>
  <meta name="description" content="Pyntacle Viewer">
  <meta name="author" content="SitePoint">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
  <link rel="stylesheet" href="http://pyntacle.css-mendel.it/css/viewer/lobipanel.css">
  <link rel="stylesheet" href="index.css">


<script src="http://pyntacle.css-mendel.it/js/sigma/stopExecutionOnTimeout.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.min.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.utils.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.polyfills.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.settings.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.captors.mouse.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.captors.touch.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.renderers.canvas.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.renderers.webgl.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.renderers.svg.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.renderers.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.webgl.nodes.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.webgl.nodes.fast.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.webgl.edges.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.webgl.edges.fast.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.webgl.edges.arrow.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.labels.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.hovers.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.nodes.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.edges.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.edges.curve.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.edges.arrow.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.edges.curvedArrow.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.edgehovers.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.edgehovers.curve.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.edgehovers.arrow.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.edgehovers.curvedArrow.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.canvas.extremities.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.svg.utils.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.svg.nodes.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.svg.edges.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.svg.edges.curve.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.svg.labels.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.svg.hovers.def.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.middlewares.rescale.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.middlewares.copy.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.misc.animation.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.misc.bindEvents.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.misc.bindDOMEvents.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.misc.drawHovers.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/sigma.plugins.tooltips.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/mustache.min.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.plugins.animate/sigma.plugins.animate.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.layout.forceAtlas2/supervisor.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.layout.forceAtlas2/worker.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.layouts.forceLink/supervisor.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.layouts.forceLink/worker.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.layouts.fruchtermanReingold/sigma.layout.fruchtermanReingold.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.layouts.dagre/sigma.layout.dagre.js"></script>

<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.plugins.relativeSize/sigma.plugins.relativeSize.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.parsers.json/sigma.parsers.json.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.parsers.gexf/sigma.parsers.gexf.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.plugins.dragNodes/sigma.plugins.dragNodes.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.plugins.filter/sigma.plugins.filter.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.exporters.image/sigma.exporters.image.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.exporters.svg/sigma.exporters.svg.js"></script>

<script src="http://pyntacle.css-mendel.it/js/viewer/jquery.1.11.min.js"></script>
<script src="http://pyntacle.css-mendel.it/js/viewer/jquery-ui.min.js"></script>
<script src="http://pyntacle.css-mendel.it/js/viewer/bootstrap.min.js"></script>
<script src="http://pyntacle.css-mendel.it/js/viewer/draggablePanel/lobipanel.min.js"></script>
<script src="http://pyntacle.css-mendel.it/js/viewer/jscolor.js"></script>
<script src="http://pyntacle.css-mendel.it/js/viewer/palette.js"></script>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@8"></script>


<script>
  function hexc(colorval) {
    var parts = colorval.match(/^rgb\\((\\d+),\\s*(\\d+),\\s*(\\d+)\\)$/);
    delete(parts[0]);
    for (var i = 1; i <= 3; ++i) {
        parts[i] = parseInt(parts[i]).toString(16);
        if (parts[i].length == 1) parts[i] = '0' + parts[i];
    }
    color = parts.join('');

    return color;
  }

  Array.prototype.remove = function() {
      var what, a = arguments, L = a.length, ax;
      while (L && this.length) {
          what = a[--L];
          while ((ax = this.indexOf(what)) !== -1) {
              this.splice(ax, 1);
          }
      }
      return this;
  };

  Object.defineProperty(Array.prototype, 'remove', {
    writeable: true,
    enumerable: false,
    value: Array.prototype.remove
  })
</script>
<script>

$(function(){

  $('.resultspanel').lobiPanel({
    reload: false,
    close: false,
    editTitle: false,
    expand: false,
    // unpin: false,
    minWidth: 430,
    minHeight: 110,
    maxWidth: 430,
    maxHeight: 480,
    resize: "both"
  });

  $('.controlspanel').lobiPanel({
    reload: false,
    close: false,
    editTitle: false,
    expand: false,
    unpin: false,
    minWidth: 260,
    minHeight: 315,
    maxWidth: 260,
    maxHeight: 395,
  });

  $('.layoutspanel').lobiPanel({
    reload: false,
    close: false,
    editTitle: false,
    expand: false,
    unpin: false,
    minWidth: 260,
    minHeight: 235,
    maxWidth: 260,
    maxHeight: 235,
    resize: "both"
  });

  var positions = [200, 320, 440, 560];
  if ($('#Key-player-results-pane').is(':visible')){
      var instancekp = $('#Key-player-results-pane').data('lobiPanel');
      instancekp.unpin();
      instancekp.setPosition(10, positions.shift());
      instancekp.enableResize();
  }

  if ($('#Group-centrality-results-pane').is(':visible')){
      var instancegc = $('#Group-centrality-results-pane').data('lobiPanel');
      instancegc.unpin();
      instancegc.setPosition(10, positions.shift());
      instancegc.enableResize();
  }

  if ($('#Communities-results-pane').is(':visible')){
    var instancecom = $('#Communities-results-pane').data('lobiPanel');
    instancecom.unpin();
    instancecom.setPosition(10, positions.shift());
    instancecom.enableResize();
  }

  if ($('#Set-results-pane').is(':visible')){
    var instanceset = $('#Set-results-pane').data('lobiPanel');
    instanceset.unpin();
    instanceset.setPosition(10, positions.shift());
    instanceset.enableResize();
  }

  var instancecontrols = $('#control-pane').data('lobiPanel');
  instancecontrols.unpin();
  instancecontrols.setPosition('right', 200)

  var instancelayouts = $('#layouts-pane').data('lobiPanel');
  instancelayouts.unpin();
  instancelayouts.setPosition('right', 560)

  var instancesolutionsgc = $('#Group-centrality-solutions-pane').data('lobiPanel');
  instancesolutionsgc.unpin();
  instancesolutionsgc.setPosition(instancegc.getPosition().x+430, instancegc.getPosition().y);
  instancesolutionsgc.enableResize();

  var instancesolutionscom = $('#Communities-solutions-pane').data('lobiPanel');
  instancesolutionscom.unpin();
  instancesolutionscom.setPosition(instancecom.getPosition().x+430, instancecom.getPosition().y);
  instancesolutionscom.enableResize();

  var instancesolutionsset = $('#Set-solutions-pane').data('lobiPanel');
  instancesolutionsset.unpin();
  instancesolutionsset.setPosition(instanceset.getPosition().x+430, instanceset.getPosition().y);
  instancesolutionsset.enableResize();
});

</script>
<script src="graph.js"></script>
<script src="report.js"></script>
<script>
  function findDepth(object){
    var level = 0;
    var key;
    for(key in object) {
        if (!object.hasOwnProperty(key)) continue;

        if(typeof object[key] == 'object'){
            var depth = findDepth(object[key]) + 1;
            level = Math.max(depth, level);
        }
    }
    return level;
}
</script>



<script>

  var nicenames_algorithms = {"KP_greedy":"Greedy", "KP_bruteforce":"Brute-force"}
  function fillDropdown(defaultkey, subkeys, dest){
      console.log("IN FUNCTION!")
      console.log(defaultkey)
      console.log(dest)
      console.log(subkeys);
      let dropdown = $('#'+dest);
      $(dropdown).empty();
      dropdown.append('<option  selected disabled hidden>'+defaultkey+'</option>');
      dropdown.prop('selectedIndex', 0);
      for(var i=0; i<subkeys.length; i++){
        console.log("ENTRY?")
        console.log(subkeys[i])
        if(subkeys[i] in nicenames_algorithms){
          label = nicenames_algorithms[subkeys[i]]
        }else{
          label = subkeys[i]
        }

        if(defaultkey=="Run"){
          console.log("this is subkeys[i] " + subkeys[i])
          date = subkeys[i].split('-')
          label = date.slice(0,3).join('-')+"-"+date[date.length-1].match(/.{2}/g).join(':');
        }
        dropdown.append($('<option></option>').attr('value', subkeys[i]).text(label))
      }
      // $.each(subkeys, function (entry) {
      //
      //   ;
      // })
  };

</script>


<script>
  function paintButtons(command, dict){
      console.log("IN PAINT")
      console.log(command)
      var solutions = JSON.stringify(dict).replace(/\\\\"/g, '"')
      $("#"+command+"-buttons").html("");
      document.getElementById(command+'-buttons').style.visibility = 'visible';
      document.getElementById(command+'-buttons').innerHTML += '<button \\
            class="btn-success" type="button" onclick=\\'popUp("'+command+'",'+solutions+')\\'>\\
                Show solutions\\
            </button>'

      // var keys = Object.keys(dict);
      // console.log(keys)
      // for(var i=0; i<keys.length; i++){
      //   document.getElementById(command+'-buttons').innerHTML += '<button \\
      //     onclick="popUp('+dict[keys[i]]+')">'+keys[i]+'</button>'
      // }
  }
</script>

<script>
  var nicenames = {"mreach":"m-reach", "group_closeness_minimum": "closeness (min)",
                   "group_closeness_mean": "closeness (mean)",
                   "group_closeness_maximum": "closeness (max)" }
  function popUp(arg,dict){
    console.log(arg)
    console.log(dict)
    if (document.getElementById(arg+'-solutions-pane')){
      document.getElementById(arg+'-solutions-pane').parentNode.removeChild(document.getElementById(arg+'-solutions-pane'));
    };
    document.getElementById(arg+"-solcol").innerHTML = '<div id="'+arg+'-solutions-pane" class="panel panel-default solutionspanel" style="display:hidden !important">\\
        <div class="panel-heading">\\
            <div class="panel-title">\\
                <h2 class="underline">'+arg.replace('-',' ').toLowerCase()+' solutions</h2>\\
            </div>\\
        </div>\\
        <div id="'+arg+'-solutions-body" class="panel-body">\\
        </div>\\
     </div>'

   $('.solutionspanel').lobiPanel({
     reload: false,
     editTitle: false,
     expand: false,
     // unpin: false,
     minWidth: 400,
     minHeight: 315,
     maxWidth: 400,
     maxHeight: 315,
     resize: "both",
   });
    var instanceresults = $('#'+arg+'-results-pane').data('lobiPanel');
    var instancesolutions = $('#'+arg+'-solutions-pane').data('lobiPanel');
    instancesolutions.unpin();
    instancesolutions.setPosition(instanceresults.getPosition().x+430, instanceresults.getPosition().y);
    instancesolutions.enableResize();

    // var instanceresults = $('#'+arg+'-results-pane').data('lobiPanel');
    // var instancesolutions = $('#'+arg+'-solutions-pane').data('lobiPanel');
    // instancesolutions.unpin();
    // instancesolutions.setPosition(instanceresults.getPosition().x+440, instanceresults.getPosition().y);
    // instancesolutions.enableResize();
    $('#'+arg+'-solutions-pane').show();
    $('#'+arg+'-solutions-body').empty()
    $('#'+arg+'-solutions-body').html("<table id='"+arg+"-table' class='table-striped solutionstable'></table>")

    for(key in dict){
      $('#'+arg+'-table').append('<tr id="'+key+'-row">')
      if(key in nicenames){
        label = nicenames[key]
      }else{
        label = key.replace('group_','').replace('_',' ')
      }

      $('#'+key+'-row').append('<td class="metric keycell">'+label+':</td>');
      console.log(dict[key]);
      console.log("SPLIT:");
      var splitsolutions = dict[key].split(';')
      console.log(splitsolutions)
      $('#'+key+'-row').append('<td id="'+key+'-solutionscell" class="solutionscell">');
      for(key2 in splitsolutions){
        console.log("KEY2")
        console.log(splitsolutions[key2])
        $('#'+key+'-solutionscell').append('<button class="btn btn-success btn-outline btn-xs solbutton"\\
                onclick="onSearch(\\''+splitsolutions[key2]+'\\'.split(\\',\\'))">'+splitsolutions[key2]+'</button>');
      }
      $('#'+key+'-row').append('</td>');
      $('#'+arg+'-table').append('</tr>');
    }
  }

</script>

</head>

<body>
  <div style="display:-webkit-box; margin-bottom:30px; margin-top:20px; text-align:-webkit-center;">
        	<img class="img-fluid" style="padding-left: 5px; padding-right:5px" src="http://pyntacle.css-mendel.it/images/pyntacle_ink.png" alt="inn_logo">
  </div>
  <div id="container">

        <!-- Import Sigma JS -->


        <!-- Add some CSS so we can see the graph! -->
        <style>
          #network-graph {
            position: absolute;
            top: 180px;
            bottom: 0;
            left: 0;
            right: 0;
          }
          body {
            color: #333;
            font-size: 14px;
            font-family: Lato, sans-serif;
          }

          #control-pane {
            /* top: 10px; */
            /*bottom: 10px;*/
            right: 10px;
            position: absolute;
            width: 230px;
            /* background-color: rgb(249, 247, 237); */
            /* box-shadow: 0 2px 6px rgba(16, 86, 0, 0.3); */
          }
          #control-pane > div {
            /* margin: 10px; */
            overflow-x: auto;
          }
          input[type="range"] {
            display: inline-block;
          }

          #layouts-pane {
            /* top: 335px !important; */
            /*bottom: 10px;*/
            right: 10px;
            position: absolute;
            width: 230px;
            /* background-color: rgb(249, 247, 237); */
            /* box-shadow: 0 2px 6px rgba(16, 86, 0, 0.3); */
          }

          #layouts-pane, .panel-minimized{
            position: unset;
          }

          #control-pane, .panel-minimized{
            position: unset;
          }

          #results-pane{
            /* left: 23px !important;
            top: 15.5px !important; */
            z-index: 10001 !important;
            width: 450px !important;
            /* right: auto !important; */
            height: 340px !important;
            /* bottom: auto !important; */
            background-color: rgb(249, 247, 237);
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
          }
          #results-pane > div {
            /* margin: 10px; */
            margin-top: 5px;
            /* overflow-x: auto; */
          }

          .buttons-div{
            display: inline-flex;
          }

          .buttons-div > select{
            flex:1 1 auto;
            height: 27px;
            width: auto;
            /* border:1px red solid; */
            text-align:center;

            margin:5px;
          }

          .buttons-div > div{
            flex:1 1 auto;
            /* border:1px red solid; */
            text-align:center;
          }

          .buttons-div > div button{
            flex:1 1 auto;
            height: 27px;
            width: auto;
            /* border:1px red solid; */
            text-align:center;

            margin:5px;
          }

          .command-header{
            color: #96764d;
            font-size: 22px;
          }
          .line {
            clear: both;
            display: block;
            width: 100%;
            margin: 0;
            padding: 12px 0 0 0;
            border-bottom: 1px solid #aac789;
            background: transparent;
          }
          h2, h3, h4 {
            padding: 0;
            font-variant: small-caps;
          }
          .green {
            color: #437356;
          }
          h2.underline {
            color: #437356;
            /* background: #f4f0e4; */
            margin: 0;
            border-radius: 2px;
            /* padding: 8px 12px; */
            font-weight: 700;
          }
          .hidden {
            display: none;
            visibility: hidden;
          }

          input[type=range] {
            width: 160px;
          }

          .sigma-tooltip {
            max-width: 440px;
            max-height: 680px;
            background-color: rgba(249, 247, 237, 0.95);
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
            border-radius: 6px;
          }

          .sigma-tooltip-header {
            font-variant: small-caps;
            font-size: 120%;
            color: #437356;
            border-bottom: 1px solid #aac789;
            padding: 10px;
          }

          .sigma-tooltip-body {
            padding: 10px;
          }

          .sigma-tooltip-body th {
            color: #999;
            text-align: left;
          }

          .sigma-tooltip-footer {
            padding: 10px;
            border-top: 1px solid #aac789;
          }

          .sigma-tooltip > .arrow {
            border-width: 10px;
            position: absolute;
            display: block;
            width: 0;
            height: 0;
            border-color: transparent;
            border-style: solid;
          }

          .sigma-tooltip.top {
            margin-top: -12px;
          }
          .sigma-tooltip.top > .arrow {
            left: 50%;
            bottom: -10px;
            margin-left: -10px;
            border-top-color: rgb(249, 247, 237);
            border-bottom-width: 0;
          }

          .sigma-tooltip.bottom {
            margin-top: 12px;
          }
          .sigma-tooltip.bottom > .arrow {
            left: 50%;
            top: -10px;
            margin-left: -10px;
            border-bottom-color: rgb(249, 247, 237);
            border-top-width: 0;
          }

          .sigma-tooltip.left {
            margin-left: -12px;
          }
          .sigma-tooltip.left > .arrow {
            top: 50%;
            right: -10px;
            margin-top: -10px;
            border-left-color: rgb(249, 247, 237);
            border-right-width: 0;
          }

          .sigma-tooltip.right {
            margin-left: 12px;
          }
          .sigma-tooltip.right > .arrow {
            top: 50%;
            left: -10px;
            margin-top: -10px;
            border-right-color: rgb(249, 247, 237);
            border-left-width: 0;
          }

    	  .sigma-tooltip > .sigma-tooltip-body > table > tbody > tr > td {
    	    padding-left: 10px;
    	    word-break: break-word;
    	  }

        .swal2-container{
          z-index:99999999;
        }

        .alertmodal{
          border: 2px solid #ceead9;
        }


        </style>

        <!-- A placeholder for the graph -->
        <div id="network-graph"></div>

        <div id="control-pane" class="panel panel-default controlspanel">
              <div class="panel-heading">
                  <div class="panel-title">
                    <h2 class="underline">filters</h2>
                  </div>
              </div>


              <div class="panel-body" style="height:auto !important">
                  <div>
                    <h3 style="margin-top: 0px; font-weight:bold">numerical attributes</h3>
                    <select id="node-numattributes">
                      <option value="" selected disabled>Choose...</option>
                    </select>
                  </div>
                  <div id ="slider-container">

                      <div id="slider-label" style="display: inline-flex; margin-top: 15px;">
                        <h4 id="attr-slider-label" style="margin-top: 0px; margin-bottom: 0px;"></h4>&nbsp
                        <span class='h4' id="min-attr-val" style="margin-top: 0px; font-weight:bold; margin-bottom: 0px">0</span>
                      </div>
                      <div>
                        <span style="vertical-align: super; ">0</span>
                        <input id="slider-attr" type="range" min="0" max="0" value="0">
                        <span id="max-attr-value" style="vertical-align: super;">0</span><br>
                        <div style="margin-bottom: 10px;">
                          <span id="survivors" class="h4" style="margin-top: 3px; font-size:16px"></span>
                        </div>
                        <div id="resize-box-container">
                          <input type="checkbox" id="resize-nodes-box" onclick="ResizeByAttr()"> Resize nodes
                        </div>
                      </div>
                  </div>
                  <div>
                    <button id="reset-btn-numerical" class="btn-danger" style="margin-top:10px;" onclick="resetNumerical()">Reset filter</button>
                  </div>

                  <div>
                    <h3 style="font-weight:bold">categorical attributes</h3>
                    <select id="node-catattributes">
                      <option value="" selected disabled>Choose...</option>
                    </select>
                  </div>
                  <div id ="multiselect-container">
                      <!-- <div id="multiselect-label" style="display: -webkit-inline-box;">
                          <h3 id="catattr-val" style="margin-top: 8px;">values for</h3>&nbsp
                          <h3 id="attr-multiselect-label" style="margin-top: 8px;"></h3>
                      </div> -->
                      <div id="multiselect-div">
                          <table id="multiselect-table" class="table table-striped table-responsive">

                          </table>
                      </div>
                  </div>
                  <div>
                    <button id="reset-btn-cat" class="btn-danger" style="margin-top:10px;" onclick="resetCat()">Reset filter</button>
                  </div>
                  <br />
                  <span class="line"></span>
                  <div>
                    <h3 style="font-weight:bold">node search</h3>
                    <input type="text" id="labelInput" size="15">
                    <button id="searchSubmit">Search</button>
                    <span id=errorspace style="font-size: 12px; margin-top: 5px; color: red; display: block;"></span>
                  </div>
              </div>
        </div>

        <div id="layouts-pane" class="panel panel-default layoutspanel">
                <div class="panel-heading">
                    <div class="panel-title">
                      <h2 class="underline">layouts</h2>
                    </div>
                </div>
                <div id="layouts-space" class="panel-body">
                      <div class="radio">
                        <label class="radio-inline"><input type="radio" name="optradio" id="radio-random" checked>Random</label>
                      </div>
                      <div class="radio">
                        <label class="radio-inline"><input type="radio" name="optradio" id="radio-circle">Circular</label>
                      </div>
                      <div class="radio">
                        <label class="radio-inline"><input type="radio" name="optradio" id="radio-atlas">ForceAtlas2</label>
                      </div>
                      <div class="radio">
                        <label class="radio-inline" data-toggle="tooltip" data-placement="top" title="For large graphs, plotting could be slow"><input type="radio" name="optradio" id="radio-frucht">Fruchterman-Reingold</label>
                        <img src="https://img.icons8.com/color/26/000000/error.png" data-toggle="tooltip" data-placement="top" style="width: 18px;" title="For large graphs, plotting could be slow">
                      </div>
                <div style="margin-top:20px">
                  <button id="export-svg" type="export">Export SVG</button>
                  <button id="export-png" type="export">Screen Shot</button>


                </div>
        </div>

        <div class="row" style="width: fit-content;">
              <div class="col-sm-6" style="width:450px; margin-left: 30px;">
                    <div id="Key-player-results-pane" class="panel panel-default resultspanel" style="display:hidden !important">
                        <div class="panel-heading">
                            <div class="panel-title">
                                <h2 class="underline">key player search</h2>
                            </div>
                        </div>
                        <div id="Key-player-results-space" class="panel-body">
                        </div>
                    </div>
              </div>
              <div class="col-sm-6" id="Key-player-solcol" style="width:450px; margin-left: 30px;">
              </div>
        </div>

        <div class="row" style="width: fit-content;">
              <div class="col-sm-6" style="width:450px; margin-left: 30px;">
                    <div id="Group-centrality-results-pane" class="panel panel-default resultspanel" style="display:hidden !important">
                        <div class="panel-heading">
                            <div class="panel-title">
                                <h2 class="underline">group centrality search</h2>
                            </div>
                        </div>
                        <div id="Group-centrality-results-space" class="panel-body">
                        </div>
                    </div>
              </div>
              <div class="col-sm-6" id="Group-centrality-solcol" style="width:450px; margin-left: 30px;">
              </div>
        </div>

        <div class="row"  style="width: fit-content;">
              <div class="col-sm-6" style="width:450px; margin-left: 30px;">
                  <div id="Communities-results-pane" class="panel panel-default resultspanel" style="display:hidden !important">
                      <div class="panel-heading">
                          <div class="panel-title">
                              <h2 class="underline">communities</h2>
                          </div>
                      </div>
                      <div id="Communities-results-space" class="panel-body">
                      </div>
                  </div>
              </div>

              <div class="col-sm-6" id="Communities-solcol" style="width:450px; margin-left: 30px;">
              </div>

        </div>




        <div class="row"  style="width: fit-content;">
              <div class="col-sm-6" style="width:450px; margin-left: 30px;">

                  <div id="Set-results-pane" class="panel panel-default resultspanel" style="display:hidden !important">
                      <div class="panel-heading">
                          <div class="panel-title">
                              <h2 class="underline">set</h2>
                          </div>
                      </div>
                      <div id="Set-results-space" class="panel-body">
                      </div>
                  </div>
            </div>

            <div class="col-sm-6" id="Set-solcol" style="width:450px; margin-left: 30px;">
            </div>
        </div>
      <!-- <div id="results-pane" class="panel panel-default">
        <div class="panel-heading">
          <div class="panel-title">
              Titolo
          </div>
        </div>
        <div class="panel-body"></div> -->
  </div>

      <!-- The most basic usage of the Sigma JSON parser -->
  <script>
        g = graphData;
        var config = {
          node: {
            // show: 'clickNode',
            // hide: 'clickStage',
            cssClass: 'sigma-tooltip',
            position: 'top',
            //autoadjust: true,
            template:
            '<div class="arrow"></div>' +
            ' <div class="sigma-tooltip-header">{{label}}</div>' +
            '  <div class="sigma-tooltip-body">' +
            '    <table id="attr-table">',
            renderer: function(node, template) {
              // The function context is s.graph
              node.degree = this.degree(node.id);
              console.log("ATTRIBUTI")
              console.log(node)
              console.log(node.attributes)
              for(n in node.attributes){
                  if(n.startsWith("__") == false && n != 'parent'){
                    console.log("attributo "+n+ " = "+ node.attributes[n])
                    template+="<tr><th>"+n+"</th> <td>"+node.attributes[n]+"</td></tr>"
                  }
              }

              template+='    </table>' +
              '  </div>' +
              '  <div class="sigma-tooltip-footer">' +
              '  Neighbors ({{degree}}): '
              // Returns an HTML string:
              console.log("Neighbors list:")
              var neighbors = this.nodeneighbors(node.id);
              var neighbors_names = [];
              for(k in neighbors){
                neighbors_names.push('<a href="#" onclick="onSearch(\\''+neighbors[k].label+'\\'.split(\\',\\'));return false;">'+neighbors[k].label+'</a>')
              }
              template+=neighbors_names.join(', ')+'  </div>';
              // console.log(this.nodeneighbors(node.id))
              return Mustache.render(template, node);

              // Returns a DOM Element:
              //var el = document.createElement('div');
              //return el.innerHTML = Mustache.render(template, node);
            }
          }
        };
        const default_Node_color = '#1b9e77'
        const SIGMA_SETTINGS = {
          labelThreshold: 7,
          // labelSize: 'proportional',
          // labelSizeRatio: 2,
          minNodeSize: 2,
          maxNodeSize: 9,
          maxEdgeSize: 3,
          edgeColor: 'default',
          defaultEdgeColor: '#D1D1D1',
          defaultNodeColor:	default_Node_color,
          maxArrowSize: 5,
          minArrowSize: 3,
          sideMargin: 10
        };

        sigma.classes.graph.addMethod('nodeneighbors', function(nodeId) {
          var k,
              neighbors = {},
              index = this.allNeighborsIndex[nodeId] || {};

          for (k in index)
            neighbors[k] = this.nodesIndex[k];

          console.log("FOUND NEIGHBORS")
          console.log(neighbors)
          return neighbors;
        });

        // Initialise sigma:
        s = new sigma(
              { // Here is the ID of the DOM element that
                // will contain the graph:
                graph : g,
                renderer: {
                  container: document.getElementById('network-graph'),
                  type: 'canvas'
                },
                settings:SIGMA_SETTINGS
              });


        function applyAtlas() {
          sigma.misc.animation.camera(
            s.camera,
            {
              ratio: 1
            },
            {duration: s.settings('animationsTime') || 500}
          );
          s.startForceAtlas2();
          window.setTimeout(function() {s.killForceAtlas2()}, 500);
        }

        function applyRandom() {

              nodes = s.graph.nodes(),
              len = nodes.length;
              for (var i = 0; i < len; i++) {
                  nodes[i].x = Math.random()*50;
                  nodes[i].y = Math.random()*50;
                  // nodes[i].color = nodes[i].center ? '#333' : '#666';
              }
              sigma.misc.animation.camera(
                s.camera,
                {
                  x: 0,
                  y: 0,
                  ratio: 1
                },
                {duration: 200}
              );
              s.refresh();
        }

        function applyFrucht(){
          sigma.misc.animation.camera(
            s.camera,
            {
              ratio: 1
            },
            {duration: s.settings('animationsTime') || 500}
          );
          var frListener = sigma.layouts.fruchtermanReingold.configure(s, {
            iterations: 500,
            easing: 'quadraticInOut',
            // duration: 800
          });

          // Bind the events:
          frListener.bind('start stop interpolate', function(e) {
            console.log(e.type);
          });

          // Start the Fruchterman-Reingold algorithm:
          sigma.layouts.fruchtermanReingold.start(s);
        }

        function applyCircular(){
          sigma.misc.animation.camera(
            s.camera,
            {
              x: 0,
              y: 0,
              ratio: 1
            },
            {duration: 200}
          );
          s.graph.nodes().forEach(function(node, i, a) {
          node.x = Math.cos(Math.PI * 2 * i / a.length)*10;
          node.y = Math.sin(Math.PI * 2 * i / a.length)*10;
          });

          //Call refresh to render the new graph
          s.refresh();
        }

        // s.refresh();


        function lookupNodesByKeyValue(sigmaInstance, key, value) {
          return sigmaInstance.graph.nodes().filter(node => node[key] === value);
        }
        function lookupNodeByKeyValue(sigmaInstance, key, value) {
          return lookupNodesByKeyValue(sigmaInstance, key, value).pop();
        }
        function lookupNodeById(sigmaInstance, value) {
          return lookupNodeByKeyValue(sigmaInstance, 'id', value);
        }
        function lookupNodeByLabel(sigmaInstance, value) {
          return lookupNodeByKeyValue(sigmaInstance, 'label', value);
        }
        function attributesToString(attr) {
          return '' +
            attr.map(function(o){
              return '' + o.attr + ' : ' + o.val + '';
            }).join('') +
            '';
        }

        var _ = {
          $: function (id) {
            return document.getElementById(id);
          },

          all: function (selectors) {
            return document.querySelectorAll(selectors);
          },

          removeClass: function(selectors, cssClass) {
            var nodes = document.querySelectorAll(selectors);
            var l = nodes.length;
            for ( i = 0 ; i < l; i++ ) {
              var el = nodes[i];
              // Bootstrap compatibility
              el.className = el.className.replace(cssClass, '');
            }
          },

          addClass: function (selectors, cssClass) {
            var nodes = document.querySelectorAll(selectors);
            var l = nodes.length;
            for ( i = 0 ; i < l; i++ ) {
              var el = nodes[i];
              // Bootstrap compatibility
              if (-1 == el.className.indexOf(cssClass)) {
                el.className += ' ' + cssClass;
              }
            }
          },

          show: function (selectors) {
            this.removeClass(selectors, 'hidden');
          },

          hide: function (selectors) {
            this.addClass(selectors, 'hidden');
          },

          toggle: function (selectors, cssClass) {
            var cssClass = cssClass || "hidden";
            var nodes = document.querySelectorAll(selectors);
            var l = nodes.length;
            for ( i = 0 ; i < l; i++ ) {
              var el = nodes[i];
              //el.style.display = (el.style.display != 'none' ? 'none' : '' );
              // Bootstrap compatibility
              if (-1 !== el.className.indexOf(cssClass)) {
                el.className = el.className.replace(cssClass, '');
              } else {
                el.className += ' ' + cssClass;
              }
            }
          }
        };


        function updatePane (graph) {
            // read nodes

            var numattr = ['degree']
            var catattr = []
            var arrayattr = []
            graph.nodes().forEach(function(n) {
              // console.log("Nodo "+n.id+" Degree: "+graph.degree(n.id))
              console.log(n.attributes);
              for(var a in n.attributes){
                if(!a.startsWith("__") && a!='name' && a!='parent'){
                  console.log(n.attributes[a]);
                  console.log("is numeric? "+ is_numeric(n.attributes[a]));
                  var isnumeric = is_numeric(n.attributes[a]);
                  if(isnumeric == "array"){
                    arrayattr.push(a)
                  }else if(isnumeric=='numeric'){
                    numattr.push(a)
                  }else if (is_numeric(n.attributes[a])=='categorical'){
                    catattr.push(a)
                  }
                }
              }
            })


            arrayattr = new Set(arrayattr);
            if(arrayattr.size>=1 && arrayattr!= undefined){
              attrlist = "<div style='font-size: 14px;'><ul>"
              arrayattr.forEach(function(u){
                attrlist+='<li style="text-align:left">'+u+'</li>';
                console.log("ATTRRR");
              });

              attrlist+='</ul></div>'
              Swal.fire({
                title: "<span style='font-size:23px;'>unavailable attributes</span>",
                html: "<span style='font-size: 14px;'>Looks like the following attribute(s) have lists as values, and they will not be plotted:</span><br /><br />"+attrlist,
                type: 'warning',
                position: 'center',
                width: '420px',
                padding: '20px',
                customClass: 'alertmodal',
                animation: 'true'

              }
              )
              // alert("The following attributes have lists as value, and they will not be plotted:\\n- "+Array.from(arrayattr).join('\\n- '))
            }
            console.log("ARRAYATTR")
            console.log(arrayattr)
            arrayattr.forEach(function(elem){
              console.log(elem+" will be removed, it's an object");

              numattr.remove(elem)
              catattr.remove(elem)
            });
            numattr = new Set(numattr);
            catattr = new Set(catattr);
            console.log("NUMATTR")
            console.log(numattr)
            AddToAttrDropdown(numattr, 'numeric', "node-numattributes")

            console.log("CATATTR")
            console.log(catattr)
            AddToAttrDropdown(catattr, 'categorical', "node-catattributes")

            // // export button
            // _.$('export-btn').addEventListener("click", function(e) {
            //   var chain = filter.export();
            //   console.log(chain);
            //   _.$('dump').textContent = JSON.stringify(chain);
            //   _.show('#dump');
            // });
        }

        // Initialize the Filter API
        filter = new sigma.plugins.filter(s);
        _.$('survivors').textContent = " "
        updatePane(s.graph);

        function applyMinAttrFilter(e) {
          var v = e.target.value;
          console.log(e)
          let attr_choice = $('#node-numattributes').val()
          total_nodes = s.graph.nodes().length
          survived_nodes = total_nodes
          console.log("V: "+v);

          if (attr_choice == 'degree'){
            filter
              .undo('attrfilter')
              .nodesBy(function(n) {
                if(s.graph.degree(n.id) < v) {
                  survived_nodes -= 1;
                }
                return s.graph.degree(n.id) >= v;
              }, 'attrfilter')
              .apply();
          }else{
            s.graph.nodes().forEach(function(n){
              console.log(Number(n.attributes[attr_choice]))
            })
            filter
              .undo('attrfilter')
              .nodesBy(function(n) {
                if(Number(n.attributes[attr_choice]) < v || n.attributes[attr_choice] == null) {
                  survived_nodes -= 1;
                }
                return Number(n.attributes[attr_choice]) >= v;
              }, 'attrfilter')
              .apply();
          }
        _.$('min-attr-val').textContent = v;
        _.$('survivors').textContent = "Nodes: "+survived_nodes+"/"+total_nodes;
          console.log("Survivors: ", survived_nodes)
        }
        _.$('slider-attr').addEventListener("input", applyMinAttrFilter);  // for Chrome and FF
        _.$('slider-attr').addEventListener("change", applyMinAttrFilter); // for IE10+, that sucks


        function AddToAttrDropdown(keyarray, attrtype, dest){
          let dropdown = $('#'+dest);
          console.log(dropdown)
          if (attrtype == 'numeric'){
            dropdown.attr("onchange", "$('#slider-container').show();\\
                           let attr_choice = $('#node-numattributes').val();\\
                           console.log('Hai scelto '+attr_choice);\\
                           var maxvalue = CalculateRange(attr_choice);\\
                            _.$('slider-attr').max = maxvalue;\\
                            _.$('max-attr-value').textContent = maxvalue;\\
                            $('#reset-btn-numerical').show();\\
                             _.$('attr-slider-label').textContent = 'min \\"'+attr_choice+'\\": '")
            // min degree
            // _.$('slider-attr').max = maxDegree;
            // _.$('max-attr-value').textContent = maxDegree;
          }else if(attrtype == 'categorical'){
            dropdown.attr("onchange", "let attr_choice = $('#node-catattributes').val();\\
                           console.log('Hai scelto '+attr_choice);\\
                           $('#multiselect-container').show();\\
                           $('#reset-btn-cat').show();\\
                           FillMultiselect(attr_choice);\\
                           ")
          }
          // dropdown.attr("onchange", 'console.log("changed '+attrtype+'")')
          for(var it = keyarray.values(), k= null; k=it.next().value; ){
            console.log("EHILA "+k)
            console.log(attrtype)
            dropdown.append($('<option></option>').attr('value', k).text(k.charAt(0).toUpperCase()+k.slice(1)))
          }
        }


        function CalculateRange(attr){
          values = []
          null_values = []
          console.log("I AM IN RANGE");
          _.$('survivors').textContent = '';
          _.$('min-attr-val').textContent = '0';
          s.graph.nodes().forEach(function(n) {
            n.color = default_Node_color;
            n.originalColor = default_Node_color;
          });
          _.$('resize-nodes-box').checked = false;
          _.$('slider-attr').value = 0;
          s.refresh();
          if (attr == 'degree'){
            var maxDegree = 0;
            s.graph.nodes().forEach(function(n) {
              maxDegree = Math.max(maxDegree, s.graph.degree(n.id));
            })
            console.log("Max for attr "+attr+" is "+maxDegree)
            $('#resize-box-container').hide()
            return maxDegree
          }else{
            s.graph.nodes().forEach(function(n) {
              values.push(Number(n.attributes[attr]));
              if(n.attributes[attr] == null){
                console.log("CAMBIA ORA");
                n.originalColor = "#ededed"
                n.color = "#ededed";
              }
            })
            s.refresh();
            console.log("Max for attr "+attr+" is "+Math.max.apply(null, values.filter(Boolean)))
            $('#resize-box-container').show()
            return Math.max.apply(null, values.filter(Boolean))
          }
        }


        function ResizeByAttr(){
          var attr = $('#node-numattributes').val()
          var status = $('#resize-nodes-box').is(':checked')
          // second create size for every node
          if(status==true && attr!='degree'){
            s.graph.nodes().forEach(function(n) {
              var attr_value = Number(n.attributes[attr]);
              n.size = Math.sqrt(attr_value);
            })
          }else{
            sigma.plugins.relativeSize(s, 1);
          }
          s.refresh();
        }

        function FillMultiselect(attr){
          var values = [];
          $('#multiselect-table').html('')
          s.graph.nodes().forEach(function(n){
              values.push(n.attributes[attr]);
          })
          let unique = [...new Set(values)];
          unique = unique.sort();
          var colors = palette('mpn65', unique.length);
          var element = $('#multiselect-table');
          if(unique.length <=65){
              console.log("CI SIAMO LENGTH A POSTO")
              for(u = 0; u < unique.length; u++){
                element.append('<tr>\\
                    <td class="col-xs-1"><input type="checkbox" name="cat-checkbox" id="'+unique[u]+'-box" onclick="update(this.checked, hexc(document.getElementById(\\''+unique[u]+'-button\\').style[\\'background-color\\']) , \\''+attr+'\\', \\''+unique[u]+'\\')"></td>\\
                    <td>'+unique[u]+'</td>\\
                    <td><button id="'+unique[u]+'-button" style="width:15px; height:15px;"></button></td>\\
                  </tr>');
                  console.log(u)
                  console.log(unique.length)

                   console.log("COLORE: "+colors[u])
                   new jscolor($('[id="'+unique[u]+'-button"]').last()[0], {valueElement:'valueElement',value:colors[u], onFineChange:'update($(\\'[id="'+unique[u]+'-box"]\\').is(\\':checked\\'), this, "'+attr+'" ,"'+unique[u]+'")'});
              }
          }else{
            console.log("MALE, torppi values, addio")
            element.append('<span style="color:red"><i>Too many values, the attribute cannot be displayed</i></span>')
          }


        }


        function update(checked, jscolor, attr, val) {
            console.log("Dsiplayed color is " + jscolor)
// 'jscolor' instance can be used as a string
        // document.getElementById('rect').style.backgroundColor = '#' + jscolor
            console.log(checked + "CHOSE "+jscolor + " for " + attr + " "+ val)
            s.graph.nodes().forEach(function(n){
                if(n.attributes[attr] == val){
                  if(checked == true){
                    console.log("changing node ")
                    console.log(n)
                    n.color = "#"+jscolor
                    n.originalColor = "#"+jscolor
                  }else{
                    n.color = default_Node_color;
                    n.originalColor = default_Node_color;
                  }
                }
            })
            s.refresh();
        }


        function resetNumerical(){
          _.$('slider-attr').value = 0;
          _.$('min-attr-val').textContent = '0';
          // _.$('resize-nodes-box').checked = false;
          // $('#survivors').hide();
          _.$('survivors').textContent = '';
          filter.undo().apply();
          // $('#node-numattributes').get(0).selectedIndex = 0;
          // _.$('slider-label').textContent = ""
        }


        function resetCat(){

          var items=document.getElementsByName('cat-checkbox');
  				for(var i=0; i<items.length; i++){
  					if(items[i].type=='checkbox'){
  						items[i].checked=false;
            }

  				}
          s.graph.nodes().forEach(function(n){
            n.color = default_Node_color;
            n.originalColor = default_Node_color;
          });
          s.refresh();
        }

        var tooltips = sigma.plugins.tooltips(s, s.renderers[0], config);
        sigma.plugins.relativeSize(s, 1);
        var popUp;
        var i,
        nodes = s.graph.nodes(),
        len = nodes.length;

        for (i = 0; i < len; i++) {
            nodes[i].x = Math.random();
            nodes[i].y = Math.random();
            // nodes[i].size = s.graph.degree(nodes[i].id);
            // nodes[i].color = nodes[i].center ? '#333' : '#666';
        }


        // We first need to save the original colors of our
        // nodes and edges, like this:
        s.graph.nodes().forEach(function(n) {
          n.originalColor = n.color;
        });
        s.graph.edges().forEach(function(e) {
          e.originalColor = e.color;
        });

        // When a node is clicked, we check for each node
        // if it is a neighbor of the clicked one. If not,
        // we set its color as grey, and else, it takes its
        // original color.
        // We do the same for the edges, and we only keep
        // edges that have both extremities colored.
        s.bind('clickNode', function(e) {
                console.log("NODE:")
                console.log(e.data.node)
                var nodeId = e.data.node.id,
                    toKeep = s.graph.nodeneighbors(nodeId);
                toKeep[nodeId] = e.data.node;
                console.log("Neighbors of "+nodeId+":")
                s.graph.nodes().forEach(function(n) {
                  if (toKeep[n.id]){
                    console.log(n)
                    n.color = "#ffa7a7";
                  }else{
                    n.color = '#ededed';
                  }

                  if (n.id == nodeId)
                      n.color = "#f00"
                });

                s.graph.edges().forEach(function(e) {
                  if (toKeep[e.target] && (e.source == nodeId || e.target == nodeId)){
                    console.log("coloring edge between "+e.source+" and "+e.target)
                    e.color = "#ffa7a7";
                    e.size = 0.3;
                  }else{
                    e.color = '#ededed';
                  }
                });

                // Since the data has been modified, we need to
                // call the refresh method to make the colors
                // update effective.
                s.refresh();

                // var prefix = s.renderers[0].options.prefix;
                // var node = e.data.node;
                // var x = e.data.node[prefix + 'x'];
                // var y = e.data.node[prefix + 'y'];

                // Manually open a tooltip on a node:
                var prefix = s.renderers[0].options.prefix;
                var node = e.data.node;
                var x = e.data.node[prefix + 'x'];
                var y = e.data.node[prefix + 'y'];
                tooltips.open(node, config.node, x, y);


                tooltips.bind('shown', function(event) {
                  console.log('tooltip shown', event);
                });

                tooltips.bind('hidden', function(event) {
                  console.log('tooltip hidden', event);
                });

        });

        function showNode(node) {
                console.log("do do do "+node.id)
        }

        // When searching
        function onSearch(query) {
                var nodes = s.graph.nodes();
                console.log(nodes);
                console.log("QUERY :"+query);
                var results = [];
                var targetNodesId = [];

                query.forEach(function(elem){
                  var r = lookupNodeByLabel(s, elem);
                  console.log("RESULT TEMP")
                  console.log(r)
                  if (r != undefined){
                    results.push(r);
                    targetNodesId.push(r.id)
                  }
                });
                if (results == []){
                  document.getElementById("errorspace").innerHTML = "Node(s) not found!";
                }else{
                  document.getElementById("errorspace").innerHTML = "";
                }
                console.log("FINAL RESULTS")
                console.log(results)
                var toKeep = {};
                var coords = {'x':0, 'y':0}
                results.forEach(function(result){
                  Object.assign(toKeep, s.graph.nodeneighbors(result.id));
                  toKeep[result.id] = result;
                  console.log("ITERATION")
                  console.log(result)

                  console.log(result.id)
                  console.log(toKeep)
                  console.log("COORDS")
                  console.log(result[s.camera.readPrefix + 'x']) //questo e' read_cam0:x
                  console.log(result[s.camera.readPrefix + 'y'])
                  coords['x']+=result[s.camera.readPrefix + 'x']
                  coords['y']+=result[s.camera.readPrefix + 'y']
                })


                // reset all previous highlights (if present)
                s.graph.nodes().forEach(function(n) {
                  n.color = n.originalColor;
                });

                s.graph.edges().forEach(function(e) {
                  e.color = e.originalColor;
                  e.size = 0;

                });

                // highlight search result and neighbors

                s.graph.nodes().forEach(function(n) {
                    if (toKeep[n.id])
                      n.color = "#ffa7a7";
                    else
                      n.color = '#ededed';

                    if (targetNodesId.includes(n.id))
                        n.color = "#f00"
                });

                s.graph.edges().forEach(function(e) {
                  // console.log("EDGE SOURCE "+e.source)
                  // console.log("EDGE target "+e.target)
                  // console.log("RESULT "+result.id)
                  // console.log(e.target == result.id)
                  console.log(toKeep[e.target])
                  if (toKeep[e.target] && (targetNodesId.includes(e.target) || targetNodesId.includes(e.source))){
                    console.log("drawing edge between "+e.source+" and "+e.target)
                    e.color = "#ffa7a7";
                    e.size = 0.3;
                  }else{
                    e.color = '#ededed';
                  }
                });

                console.log("AVG COORDS")
                console.log(coords['x']/results.length)
                console.log(coords['y']/results.length)

                sigma.misc.animation.camera(
                  s.camera,
                  {
                    x: coords['x']/results.length,
                    y: coords['y']/results.length,

                  },
                  {duration: s.settings('animationsTime') || 300}
                );
                s.refresh();
        }

        // When the stage is clicked, we just color each
        // node and edge with its original color.
        s.bind('clickStage', function(e) {
          tooltips.close();

          s.graph.nodes().forEach(function(n) {
            n.color = n.originalColor;
          });

          s.graph.edges().forEach(function(e) {
            e.color = e.originalColor;
            e.size = 0;

          });

          // Same as in the previous event:
          s.refresh();
        });

        s.cameras[0].bind('coordinatesUpdated', function() {
          tooltips.close();
        });


        var dragListener = sigma.plugins.dragNodes(s, s.renderers[0]);

        dragListener.bind('startdrag', function(event) {
          tooltips.close();
          console.log(event);
        });
        dragListener.bind('drag', function(event) {
          tooltips.close();

          console.log(event);
        });
        dragListener.bind('drop', function(event) {
          console.log(event);
        });
        dragListener.bind('dragend', function(event) {
          console.log(event);
        });


        function SearchByLabel(e) {
          var v = document.getElementById('labelInput').value.split(',')
          console.log("MYQUERY")
          console.log(v)
          onSearch(v)
          // var c = e.target[e.target.selectedIndex].value;
          // filter
          //   .undo('node-category')
          //   .nodesBy(function(n) {
          //     return !c.length || n.attributes.acategory === c;
          //   }, 'node-category')
          //   .apply();
        }

        _.$('searchSubmit').addEventListener("click", SearchByLabel);  // for Chrome and FF


        var ex1 = document.getElementById('radio-random');
        var ex2 = document.getElementById('radio-atlas');
        var ex3 = document.getElementById('radio-frucht');
        var ex4 = document.getElementById('radio-circle');


        ex1.onclick = applyRandom;
        ex2.onclick = applyAtlas;
        ex3.onclick = applyFrucht;
        ex4.onclick = applyCircular;


        $('#slider-container').hide();
        $('#reset-btn-numerical').hide();
        $('#reset-btn-cat').hide();
        $('#multiselect-container').hide();
        if (document.getElementById('Key-player-results-pane') !== null){
          $('#Key-player-results-pane').hide();
          $('#Key-player-solutions-pane').hide();
        }

        if (document.getElementById('Group-centrality-results-pane') !== null){
          $('#Group-centrality-results-pane').hide();
          $('#KGroup-centrality-solutions-pane').hide();
        }

        if (document.getElementById('Communities-results-pane') !== null){
          $('#Communities-results-pane').hide();
          $('#Communities-solutions-pane').hide();
        }

        if (document.getElementById('Set-results-pane') !== null){
          $('#Set-results-pane').hide();
          $('#Set-solutions-pane').hide();

        }

        // if (document.getElementById('Communities-results-pane') !== null){
        //   document.getElementById('Communities-results-pane').style.visibility = 'hidden';
        // }
        // if (document.getElementById('Set-results-pane') !== null){
        //   document.getElementById('Set-results-pane').style.visibility = 'hidden';
        // }

          // var s = new sigma()
        console.log("REPORT")
        console.log(reportData)

        for (var command in reportData){
          console.log("BUILDING "+ command)
          $('#'+command+'-results-pane').show();
          document.getElementById(command+'-results-space').innerHTML += '<div class="buttons-div" id="'+command+'-section"></div>';

          document.getElementById(command+'-section').innerHTML += '\\
            <select \\
                class="btn-secondary" id="dropdown-'+command+'-algorithm" \\
                onchange="\\
                  document.getElementById(\\'dropdown-'+command+'-run\\').style.visibility = \\'visible\\'; \\
                  document.getElementById(\\''+command+'-buttons\\').style.visibility = \\'hidden\\'; \\
                  $(\\'#'+command+'-solutions-pane\\').lobiPanel(\\'close\\'); \\
                  var choice = getChoice(\\'dropdown-'+command+'-algorithm\\'); \\
                  fillDropdown(\\'Run\\', Object.keys(reportData[\\''+command+'\\'][choice]), \\'dropdown-'+command+'-run\\')\\
                "\\
            >\\
            </select>';

          document.getElementById(command+'-section').innerHTML += '\\
            <select \\
                class="btn-secondary" id="dropdown-'+command+'-run" \\
                onchange="\\
                  var choice = getChoice(\\'dropdown-'+command+'-algorithm\\'); \\
                  var choice2 = getChoice(\\'dropdown-'+command+'-run\\'); \\
                  console.log(reportData[\\''+command+'\\'][choice][choice2]);\\
                  paintButtons(\\''+command+'\\', reportData[\\''+command+'\\'][choice][choice2]);\\
                "\\
            >\\
            </select><div id="'+command+'-buttons"></div>';

          document.getElementById('dropdown-'+command+'-run').style.visibility = 'hidden';
          fillDropdown('Algorithm', Object.keys(reportData[command]), 'dropdown-'+command+'-algorithm');
          // console.log(reportData[command])
          // console.log(findDepth(reportData[command]))

        };
        // load the graph
        // s.graph.read(graph);
        // call the plugin
        // draw the graph

        function getChoice(dropd){
          var a = document.getElementById(dropd);
          return a.options[a.selectedIndex].value
        }

        function is_numeric(str){
            if(typeof str == 'object' && str != null){
              return "array";
            }else if(str != null && !isNaN(str)){
      		    return "numeric";
      	    }else if (typeof(str)=='string'){
      		    return "categorical";
            }
        }


        document.getElementById('export-svg').onclick = function() {
          console.log('exporting...');
          var output = s.toSVG({download: true, filename: 'mygraph.svg', width: 1920, height:1080, labels: true,});
          // console.log(output);
        };


        function generateImage(mouse, clip) {
          console.log(mouse)
          console.log(clip)
          var size = 0;
          var color = "#FFFFFF";
          console.log(size);
          console.log(color);
          console.log(s.renderers)
          sigma.plugins.image(s, s.renderers[0], {
            download: true,
            size: size,
            margin: 50,
            background: color,
            clip: clip,
            zoomRatio: 1,
            labels: true
          });
        }

      _.$('export-png').addEventListener("click", function(event) {
  generateImage(event, true)
});
      s.refresh()
      applyRandom();

  </script>
  <!-- <div class="modal fade" id="warningModal" tabindex="-1" role="dialog" aria-labelledby="warningModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="warningModalLabel">Modal title</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          ...
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div> -->

</body>

</html>


"""



css_template = u"""







#network-graph {
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      position: absolute;
    }

    .sigma-tooltip {
      max-width: 240px;
      max-height: 280px;
      background-color: rgb(249, 247, 237);
      box-shadow: 0 2px 6px rgba(0,0,0,0.3);
      border-radius: 6px;
    }

    .sigma-tooltip-header {
      font-variant: small-caps;
      font-size: 120%;
      color: #437356;
      border-bottom: 1px solid #aac789;
      padding: 10px;
    }

    .sigma-tooltip-body {
      padding: 10px;
    }

    .sigma-tooltip-body th {
      color: #999;
      text-align: left;
    }

    .sigma-tooltip-footer {
      padding: 10px;
      border-top: 1px solid #aac789;
    }

    .sigma-tooltip > .arrow {
      border-width: 10px;
      position: absolute;
      display: block;
      width: 0;
      height: 0;
      border-color: transparent;
      border-style: solid;
    }

    .sigma-tooltip.top {
      margin-top: -12px;
    }
    .sigma-tooltip.top > .arrow {
      left: 50%;
      bottom: -10px;
      margin-left: -10px;
      border-top-color: rgb(249, 247, 237);
      border-bottom-width: 0;
    }

    .sigma-tooltip.bottom {
      margin-top: 12px;
    }
    .sigma-tooltip.bottom > .arrow {
      left: 50%;
      top: -10px;
      margin-left: -10px;
      border-bottom-color: rgb(249, 247, 237);
      border-top-width: 0;
    }

    .sigma-tooltip.left {
      margin-left: -12px;
    }
    .sigma-tooltip.left > .arrow {
      top: 50%;
      right: -10px;
      margin-top: -10px;
      border-left-color: rgb(249, 247, 237);
      border-right-width: 0;
    }

    .sigma-tooltip.right {
      margin-left: 12px;
    }
    .sigma-tooltip.right > .arrow {
      top: 50%;
      left: -10px;
      margin-top: -10px;
      border-right-color: rgb(249, 247, 237);
      border-left-width: 0;
    }
h1 {
      margin-bottom: 5px;
      margin-top: 5px;
}
h2, .h2 {
    font-size: 23px;
}
h3, .h3 {
    font-size: 20px;
}

h4, .h4 {
    font-variant: all-small-caps !important;
}

hr {
    margin-top: 5px;
    margin-bottom: 15px;
    border-color: #d3c6b1;
}

.panel{
  border: 1px solid transparent;
}

.panel-default>.panel-heading{
  background-color: #ceead9;
    border-color: #647d6c;
}

.lobipanel.panel-unpin {
  -webkit-box-shadow: 0 2px 6px rgba(16, 86, 0, 0.3);
  box-shadow: 0 2px 6px rgba(16, 86, 0, 0.3);
}


button {
  -webkit-appearance: button-bevel;
}


.btn-secondary {
    color: #fff;
    background-color: #466279;
    border-color: #466279;
  }

.btn-secondary:hover, .btn-secondary:active, .btn-secondary.active, .open > .dropdown-toggle.btn-secondary {
    color: #fff;
    background-color: #1c4363;
    border-color: #1c4363;
}

.btn-secondary:focus, .btn-secondary.focus > .dropdown-toggle.btn-secondary {
  color: #fff;
  background-color: #2d618e;
  border-color: #2d618e;

}

.btn-success {
    color: #fff;
    background-color: #588c58;
    border-color: #4cae4c;
}


select option {
    background: #FFFFFF;
    color: #000000;

}

#draggablePanelList .panel-heading {
       cursor: move;
   }
#draggablePanelList2 .panel-heading {
       cursor: move;
   }

  .lobipanel-minimized-toolbar{
    background: none;
   /*height: 45px;*/
  }

.solution{
    color: #4a8fea;
    margin-left: 10px;
}

.solutionstable {
    table-layout: fixed; 
    width: -webkit-fill-available;
}
.keycell{
    width:37%; 
    padding: 5px;
    vertical-align: top;
    font-weight: bold;
}
.solutionscell{
    width:-webkit-fill-available;
    padding: 8px 0 3px 0;
    word-wrap: break-word; 
    float: left;
}
.solbutton{
    background-color:#ffffff;
    color:#000000;
    -webkit-appearance: unset !important;
    padding: 0px 3px;
    margin-right: 5px;
    margin-bottom: 5px;
}

input[type=checkbox] {
  margin: 0;
  vertical-align: middle;
  position: relative;
  bottom: 1px;
}

#multiselect-table>tbody>tr>td {
    word-break: break-word;
    padding: 4px;
    border-top: 0px solid #ddd;
}

#multiselect-div{
    padding: 5px;
    margin-top: 15px;
    border: 1px solid #ceead9;
}



"""