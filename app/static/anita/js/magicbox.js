(function() {
  var contentEditor = angular.module("contentEditor", []);
  
    // To create a empty resizable and draggable box
  contentEditor.directive("magicboxCreator", function($document, $compile) {
    return {
      restrict: 'A',
      link: function($scope, $element, $attrs) {
        $element.on("mousedown", function($event) {
          var newNode = $compile('<div class="contentEditorBox" ce-drag ce-resize></div>')($scope);
          
          newNode.css({
                position: "absolute",
            top: $event.pageY - 25 + "px",
            left: $event.pageX - 25 + "px",
                });
          
          angular.element($document[0].body).append(newNode);
        });
      }
    }
  });
  
    // To manage the drag
  contentEditor.directive("ceDrag", function($document) {
      return function($scope, $element, $attr) {
          var startX = 0, startY = 0;
      var newElement = angular.element('<div class="draggable"></div>');
      
      $element.append(newElement);
          newElement.on("mousedown", function($event) {
            $event.preventDefault();
            
                // To keep the last selected box in front
            angular.element(document.querySelectorAll(".contentEditorBox")).css("z-index", "0");
            $element.css("z-index", "1"); 
            
            startX = $event.pageX - $element[0].offsetLeft;
            startY = $event.pageY - $element[0].offsetTop;
            $document.on("mousemove", mousemove);
            $document.on("mouseup", mouseup);
          });
          
          function mousemove($event) {
            y = $event.pageY - startY;
            x = $event.pageX - startX;
            $element.css({
              top: y + "px",
              left:  x + "px"
            });
          }
          
          function mouseup() {
            $document.off("mousemove", mousemove);
            $document.off("mouseup", mouseup);
          }
        };
      });
  
    // To manage the resize
  contentEditor.directive("ceResize", function($document) {
    return function($scope, $element, $attr) {
      
            // Function to manage resize up event
      var resizeUp = function($event) {
        var top = $event.pageY;
        var height = $element[0].offsetTop + $element[0].offsetHeight - $event.pageY;
        
        if ($event.pageY < $element[0].offsetTop + $element[0].offsetHeight - 50) {
          $element.css({
            top: top + "px",
            height: height + "px"
          });
        } else {
          $element.css({
            top: $element[0].offsetTop + $element[0].offsetHeight - 50 + "px",
            height: "50px"
          }); 
        }
      };
      
            // Function to manage resize right event
      var resizeRight = function($event) {
        var width = $event.pageX - $element[0].offsetLeft;
        
        if ($event.pageX > $element[0].offsetLeft + 50) {
          $element.css({
            width: width + "px"
          });
        } else {
          $element.css({
            width: "50px",
          });
        }
      };
      
            // Function to manage resize down event
      var resizeDown = function($event) {
        var height = $event.pageY - $element[0].offsetTop;
        
        if ($event.pageY > $element[0].offsetTop + 50) {
          $element.css({
            height: height + "px"
          });
        } else {
          $element.css({
            height: "50px"
          });
        }
      };
      
            // Function to manage resize left event
      var resizeLeft = function($event) {
        var left = $event.pageX;
        var width = $element[0].offsetLeft + $element[0].offsetWidth - $event.pageX;
        
        if ($event.pageX < $element[0].offsetLeft + $element[0].offsetWidth - 50) {
          $element.css({
            left: left + "px",
            width: width + "px"
          });
        } else {
          $element.css({
            left: $element[0].offsetLeft + $element[0].offsetWidth - 50 + "px",
            width: "50px"
          });
        }
      };
      
            // Create a div to catch resize up event
      var newElement = angular.element('<div class="n-resize"></div>');
      $element.append(newElement);
      newElement.on("mousedown", function() {
        $document.on("mousemove", mousemove);
        $document.on("mouseup", mouseup);
        
            function mousemove($event) {
              $event.preventDefault();
              resizeUp($event);
            }
            
            function mouseup() {
              $document.off("mousemove", mousemove);
              $document.off("mouseup", mouseup);
            }
      });
      
            // Create a div to catch resize right event
      newElement = angular.element('<div class="e-resize"></div>');
      $element.append(newElement);
      newElement.on("mousedown", function() {
        $document.on("mousemove", mousemove);
            $document.on("mouseup", mouseup);
            
            function mousemove($event) {
              $event.preventDefault();
              resizeRight($event);
            }
            
            function mouseup() {
              $document.off("mousemove", mousemove);
              $document.off("mouseup", mouseup);
            }
      });
      
            // Create a div to catch resize down event
      newElement = angular.element('<div class="s-resize"></div>');
      $element.append(newElement);
      newElement.on("mousedown", function() {
        $document.on("mousemove", mousemove);
        $document.on("mouseup", mouseup);
        
            function mousemove($event) {
              $event.preventDefault();
              resizeDown($event);
            }
            
            function mouseup() {
              $document.off("mousemove", mousemove);
              $document.off("mouseup", mouseup);
            }
      });
      
            // Create a div to catch resize left event
      newElement = angular.element('<div class="w-resize"></div>');
      $element.append(newElement);
      newElement.on("mousedown", function() {
        $document.on("mousemove", mousemove);
        $document.on("mouseup", mouseup);
        
            function mousemove($event) {
              $event.preventDefault();
              resizeLeft($event);
            }
            
            function mouseup() {
              $document.off("mousemove", mousemove);
              $document.off("mouseup", mouseup);
            }
      });
      
            // Create a div to catch resize up left event
      newElement = angular.element('<div class="nw-resize"></div>');
      $element.append(newElement);
      newElement.on("mousedown", function() {
        $document.on("mousemove", mousemove);
        $document.on("mouseup", mouseup);
        
            function mousemove($event) {
              $event.preventDefault();
              resizeUp($event);
              resizeLeft($event);
            }
            
            function mouseup() {
              $document.off("mousemove", mousemove);
              $document.off("mouseup", mouseup);
            }
      });
      
            // Create a div to catch resize up right event
      newElement = angular.element('<div class="ne-resize"></div>');
      $element.append(newElement);
      newElement.on("mousedown", function() {
        $document.on("mousemove", mousemove);
        $document.on("mouseup", mouseup);
        
            function mousemove($event) {
              $event.preventDefault();
              resizeUp($event);
              resizeRight($event);
            }
            
            function mouseup() {
              $document.off("mousemove", mousemove);
              $document.off("mouseup", mouseup);
            }
      });
      
            // Create a div to catch resize down right event
      newElement = angular.element('<div class="se-resize"></div>');
      $element.append(newElement);
      newElement.on("mousedown", function() {
        $document.on("mousemove", mousemove);
        $document.on("mouseup", mouseup);
        
            function mousemove($event) {
              $event.preventDefault();
              resizeDown($event);
              resizeRight($event);
            }
            
            function mouseup() {
              $document.off("mousemove", mousemove);
              $document.off("mouseup", mouseup);
            }
      });
      
            // Create a div to catch resize down left event
      newElement = angular.element('<div class="sw-resize"></div>');
      $element.append(newElement);
      newElement.on("mousedown", function() {
        $document.on("mousemove", mousemove);
        $document.on("mouseup", mouseup);
            
            function mousemove($event) {
              $event.preventDefault();
              resizeDown($event);
              resizeLeft($event);
            }
            
            function mouseup() {
              $document.off("mousemove", mousemove);
              $document.off("mouseup", mouseup);
            }
      });
    };
  });
})();