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
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.layout.forceAtlas2/supervisor.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.layout.forceAtlas2/worker.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.plugins.relativeSize/sigma.plugins.relativeSize.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.parsers.json/sigma.parsers.json.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.parsers.gexf/sigma.parsers.gexf.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.plugins.dragNodes/sigma.plugins.dragNodes.js"></script>
<script src="http://pyntacle.css-mendel.it/js/sigma/plugins/sigma.plugins.filter/sigma.plugins.filter.js"></script>
<script src="http://pyntacle.css-mendel.it/js/viewer/jquery.1.11.min.js"></script>
<script src="http://pyntacle.css-mendel.it/js/viewer/jquery-ui.min.js"></script>
<script src="http://pyntacle.css-mendel.it/js/viewer/bootstrap.min.js"></script>
<script src="http://pyntacle.css-mendel.it/js/viewer/draggablePanel/lobipanel.min.js"></script>
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
    // unpin: false,
    minWidth: 230,
    minHeight: 315,
    maxWidth: 230,
    maxHeight: 315,
    resize: "both"

  });

  $('.solutionspanel').lobiPanel({
    reload: false,
    editTitle: false,
    expand: false,
    // unpin: false,
    minWidth: 330,
    minHeight: 315,
    maxWidth: 330,
    maxHeight: 315,
    resize: "both",


  });
  var positions = [10, 130, 250];
  if ($('#Key-player-results-pane').is(':visible')){
      var instancekp = $('#Key-player-results-pane').data('lobiPanel');
      instancekp.unpin();
      instancekp.setPosition(10, positions.shift());
      instancekp.enableResize();
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
  instancecontrols.setPosition('right', 10)

  var instancesolutionskp = $('#Key-player-solutions-pane').data('lobiPanel');
  instancesolutionskp.unpin();
  instancesolutionskp.setPosition(instancekp.getPosition().x+430, instancekp.getPosition().y);
  instancesolutionskp.enableResize();

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
  function fillDropdown(defaultkey, subkeys, dest){
      console.log("IN FUNCTION!")
      console.log(subkeys);
      let dropdown = $('#'+dest);
      $(dropdown).empty();
      console.log(dest)
      dropdown.append('<option  selected disabled hidden>'+defaultkey+'</option>');
      dropdown.prop('selectedIndex', 0);
      for(var i=0; i<subkeys.length; i++){
        console.log("ENTRY?")
        console.log(subkeys[i])
        dropdown.append($('<option></option>').attr('value', subkeys[i]).text(subkeys[i]))
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
  function popUp(arg,dict){
    console.log(arg)
    console.log(dict)
    var instanceresults = $('#'+arg+'-results-pane').data('lobiPanel');
    var instancesolutions = $('#'+arg+'-solutions-pane').data('lobiPanel');
    instancesolutions.unpin();
    instancesolutions.setPosition(instanceresults.getPosition().x+440, instanceresults.getPosition().y);
    instancesolutions.enableResize();
    $('#'+arg+'-solutions-pane').show();
    $('#'+arg+'-solutions-body').empty()
    for(key in dict){
      $('#'+arg+'-solutions-body').append('<span class="metric">'+key+':</span>');
      console.log(dict[key])
      console.log("SPLIT:")
      var splitsolutions = dict[key].split(';')
      for(key2 in splitsolutions){
        $('#'+arg+'-solutions-body').append('<span class="solution"\\
                onclick="onSearch(\\''+splitsolutions[key2]+'\\'.split(\\',\\'))"><u>'+splitsolutions[key2]+'</u></span>');
      }
      $('#'+arg+'-solutions-body').append('<br />');
    }
  }

</script>

</head>

<body>
  <div id="container">

        <!-- Import Sigma JS -->


        <!-- Add some CSS so we can see the graph! -->
        <style>
          #network-graph {
            top: 0;
            bottom: 0;
            left: 0;
            right: 0;
            position: absolute;
          }
          body {
            color: #333;
            font-size: 14px;
            font-family: Lato, sans-serif;
          }

          #control-pane {
            top: 10px;
            /*bottom: 10px;*/
            right: 10px;
            position: absolute;
            width: 230px;
            /* background-color: rgb(249, 247, 237); */
            box-shadow: 0 2px 6px rgba(16, 86, 0, 0.3);
          }
          #control-pane > div {
            /* margin: 10px; */
            overflow-x: auto;
          }
          input[type="range"] {
            display: inline-block;
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
            max-width: 240px;
            max-height: 280px;
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
        </style>

        <!-- A placeholder for the graph -->
        <div id="network-graph"></div>

        <div id="control-pane" class="panel panel-default controlspanel">
          <div class="panel-heading">
              <div class="panel-title">
                <h2 class="underline">filters</h2>
              </div>
          </div>


          <div class="panel-body">
              <div>
                <h3>min degree <span id="min-degree-val">0</span></h3>
                  0 <input id="min-degree" type="range" min="0" max="0" value="0"> <span id="max-degree-value">0</span><br>
              </div>

              <div>
                <h3>node search</h3>
                <input type="text" id="labelInput" size="15">
                <button id="searchSubmit">Search</button>
                <span id=errorspace style="font-size: 12px; margin-top: 5px; color: red; display: block;"></span>
              </div>
              <span class="line"></span>
              <div>
                <button id="reset-btn">Reset filters</button>
                <button id="export-btn">Export</button>
              </div>
              <div id="dump" class="hidden"></div>
            </div>
          </div>

          <div class="row">
              <div class="col-sm-6" style="width:450px; margin-left: 30px;">
                    <div id="Key-player-results-pane" class="panel panel-default resultspanel" style="display:hidden !important">
                        <div class="panel-heading">
                            <div class="panel-title">
                                <h2 class="underline">key-player</h2>
                            </div>
                        </div>
                        <div id="Key-player-results-space" class="panel-body">
                        </div>
                    </div>
              </div>
              <div class="col-sm-6" style="width:450px; margin-left: 30px;">
                    <div id="Key-player-solutions-pane" class="panel panel-default solutionspanel" style="display:hidden !important">
                      <div class="panel-heading">
                          <div class="panel-title">
                              <h2 class="underline">key-player solutions</h2>
                          </div>
                      </div>
                      <div id="Key-player-solutions-body" class="panel-body">
                      </div>
                   </div>
              </div>
          </div>


          <div class="row">
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

              <div class="col-sm-6" style="width:450px; margin-left: 30px;">
                    <div id="Communities-solutions-pane" class="panel panel-default solutionspanel" style="display:hidden !important">
                      <div class="panel-heading">
                          <div class="panel-title">
                              <h2 class="underline">communities solutions</h2>
                          </div>
                      </div>
                      <div id="Communities-solutions-body" class="panel-body">
                      </div>
                   </div>
              </div>

          </div>


          <div class="row">
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

            <div class="col-sm-6" style="width:450px; margin-left: 30px;">
                  <div id="Set-solutions-pane" class="panel panel-default solutionspanel" style="display:hidden !important">
                    <div class="panel-heading">
                        <div class="panel-title">
                            <h2 class="underline">set solutions</h2>
                        </div>
                    </div>
                    <div id="Set-solutions-body" class="panel-body">
                    </div>
                 </div>
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
                  if(n.startsWith("__") == false){
                    console.log("attributo "+n+ " = "+ node.attributes[n])
                    template+="<tr><th>"+n+"</th> <td>"+node.attributes[n]+"</td></tr>"
                  }
              }
              template+='    </table>' +
              '  </div>' +
              '  <div class="sigma-tooltip-footer">Number of connections: {{degree}}</div>'
              // Returns an HTML string:
              return Mustache.render(template, node);

              // Returns a DOM Element:
              //var el = document.createElement('div');
              //return el.innerHTML = Mustache.render(template, node);
            }
          }
        };

        const SIGMA_SETTINGS = {
          labelThreshold: 7,
          // labelSize: 'proportional',
          // labelSizeRatio: 2,
          minNodeSize: 2,
          maxNodeSize: 9,
          maxEdgeSize: 6,
          edgeColor: 'default',
          defaultEdgeColor: '#D1D1D1',
          maxArrowSize: 5,
          minArrowSize: 3,
          sideMargin: 10
        };

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


        function updatePane (graph, filter) {
          // get max degree
          var maxDegree = 0,
              categories = {};

          // read nodes
          graph.nodes().forEach(function(n) {
            console.log("Nodo "+n.id+" Degree: "+graph.degree(n.id))
            maxDegree = Math.max(maxDegree, graph.degree(n.id));
            console.log(maxDegree)
            // categories[n.attributes.acategory] = true;
          })

          // min degree
          _.$('min-degree').max = maxDegree;
          _.$('max-degree-value').textContent = maxDegree;

          // reset button
          _.$('reset-btn').addEventListener("click", function(e) {
            _.$('min-degree').value = 0;
            _.$('min-degree-val').textContent = '0';
            filter.undo().apply();
            _.$('dump').textContent = '';
            _.hide('#dump');
          });

          // export button
          _.$('export-btn').addEventListener("click", function(e) {
            var chain = filter.export();
            console.log(chain);
            _.$('dump').textContent = JSON.stringify(chain);
            _.show('#dump');
          });
        }



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

                    console.log("ENTRATO")
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

                    s.refresh();
                    // launch force-atlas for 5sec
                    s.startForceAtlas2();
                    window.setTimeout(function() {s.killForceAtlas2()}, 1000);
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
                        e.color = "#b00";
                        e.size = 0.5;
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
                        e.color = "#b00";
                        e.size = 0.5;
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
                        ratio: 1
                      },
                      {duration: s.settings('animationsTime') || 300}
                    );
                    s.refresh();



                    // Filter or find the first matching node then apply showNode on it
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

                // Initialize the Filter API
                filter = new sigma.plugins.filter(s);

                updatePane(s.graph, filter);

                function applyMinDegreeFilter(e) {
                  var v = e.target.value;
                  console.log("V: "+v);
                  _.$('min-degree-val').textContent = v;

                  filter
                    .undo('min-degree')
                    .nodesBy(function(n) {
                      return s.graph.degree(n.id) >= v;
                    }, 'min-degree')
                    .apply();
                }

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

                _.$('min-degree').addEventListener("input", applyMinDegreeFilter);  // for Chrome and FF
                _.$('min-degree').addEventListener("change", applyMinDegreeFilter); // for IE10+, that sucks
                _.$('searchSubmit').addEventListener("click", SearchByLabel);  // for Chrome and FF


        if (document.getElementById('Key-player-results-pane') !== null){
          $('#Key-player-results-pane').hide();
          $('#Key-player-solutions-pane').hide();

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
        </script>


    </div>

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
    background-color: #2d618e;
    border-color: #2d618e;
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
    height: 45px;
  }

.solution{
    color: #4a8fea;
    margin-left: 10px;
}


"""