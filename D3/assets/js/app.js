// @TODO: YOUR CODE HERE!
// read the data from the csv file 

// set up the defalut views for x and y on page load
var xView = "poverty";
var yView = "healthcare";

d3.csv(".\\assets\\data\\data.csv").then(function(dataset){
        
        showVisual(dataset, xView, yView); 
        
});

// Create the svg canvas height and width 

var svgHeight = 500;
var svgWidth = 900; 

// margins to move your svg to the down and to the right 

var margin = {
    top: 50, 
    right: 50,
    bottom: 20, 
    left: 50
}

var padding = {
    top: -49,
    right: 19,
    left: 0
}

// Adjust your svg position 
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;


// Append svg to the index.html 
var svg = d3.select("#scatter")
          .append("svg")
          .attr("width", width)
          .attr("height", height) 
          .attr("class", "scatter")
          .append("g")
          .attr("tranform", `translate( ${margin.left}, ${margin.top})`);


function showVisual(data, xView, yView){

    data.map(d =>{
       // I've only cleans a small sample of the data. 
       // you will need to handle the rest
        data.poverty = +d[xView];
        data.healthcare = +d[yView];
        
    });

 // we need to get the min and max of x & y in the dataset to pass to .domain()
var xValues  = data.map(d => parseFloat(d[xView]));
var yValues  = data.map(d => parseFloat(d[yView])); 


// use extent to grab the min and max of the selected Scale and Axis
var xScale = d3.scaleLinear()
            .domain(d3.extent(xValues))
            .range([margin.right + 19, width+margin.right]);

var yScale = d3.scaleLinear()
            .domain(d3.extent(yValues))
            .range([height-37, margin.top]); 

// Add the x & y Axis
var xAxis = d3.axisBottom(xScale);
var yAxis = d3.axisLeft(yScale);



// add the x & y scales to the index.html <svg> tag 
svg.append("g")
        .attr("class", "xAxis")
        .attr("transform", `translate(${padding.top},  ${height - margin.bottom})`)
        .call(xAxis);

svg.append("g")
        .attr("class", "yAxis")
        .attr("transform", `translate(${padding.right}, ${padding.right -4})`)
        .call(yAxis);

// Create the <circle></circle> element 

var scatter = svg.selectAll("circle")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", d => xScale( d[xView] ))
            .attr("cy", d => yScale( d[yView] ))
            .attr("r", 10).style("fill", "blue") 
            .attr("opacity", ".5");

// text in circles

svg.selectAll("text")
            .data(data)
            .enter()
            .append("text")
            .attr("x", d => xScale( d[xView] ) )
            .attr("y", d => yScale( d[yView] ) )
            .attr("font-size", 10)
            .attr("text-anchor", "middle")
            .style("fill", "white")
            .text( d => d.abbr);
     

// y axis
// chart group
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

chartgroup.append("text")
     .attr("transform", "rotate(-90)")
     .attr("y", 40 - margin.left)
     .attr("x", 0 - (height / 2))
     .attr("dy", "1em")
     .classed("aText", true)
     .text("Lacking Healthcare (%)");

// x axis
chartGroup.append("text")
     .attr("y", height + margin.bottom/2 - 10)
     .attr("x", width / 2)
     .attr("dy", "1em")
     .classed("aText", true)
     .text("Poverty Rate (%)");
/* data[xView] is the name of the scale that will be 
    the name of the scale that is clicked and updated
    you will need to update the bubbles with:

    1. Text for state abbr      
    2. Event Handlers 
    3. Labels that the user will click to update the chart 
    4. colors for bubbles and abbr state letters

  */          
 console.log("data", data[xView]);

  }
