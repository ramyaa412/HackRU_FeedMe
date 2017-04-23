
// var cuisine = document.getElementById("cuisine");
// var distance = document.getElementById("distance");
// var price = document.getElementById("price");	
var submitUser = document.getElementById("submit");

var cUser;
var dUser;
var pUser;
var name;
var distance;
var rating;
var address;
var meal;
var calories;

var arrRating = [4.3, 5.0, 2.5, 4.2, 4.8, 4.1, 3.8];
var arrName = ["Dona Bella", "El mar", "Per Se", "Mariella", "ABC Kitchen", "The Smith", "Uplnd"];
var arrAddress = ["1 Lawrence Drive, Princeton, NJ", "2 Lawrence Drive, Princeton, NJ", "3 Lawrence Drive, Princeton, NJ", "4 Lawrence Drive, Princeton, NJ",
 "5 Lawrence Drive, Princeton, NJ", "6 Lawrence Drive, Princeton, NJ", "7 Lawrence Drive, Princeton, NJ"];
 var arrMeal = ["Chicken Grill Sandwich", "Fajita Vegetables", "California Pizza Kitchen", "Chili's Grill", "Grilled Salmon",
  "Sizzling Chicken and Spinach", "The Buttermilk Oven-Fried Tofu"];
 var arrCalories = ["400 Calories", "380 Calories", "360 Calories", "420 Calories", "415 Calories", "340 Calories", "390 Calories"];


	submitUser.addEventListener("click", function() {
		cUser = $('#cuisineUser').val();
		dUser = $('#distanceUser').val();
		pUser = $('#priceUser').val();
		var random = Math.floor(Math.random()*7);
		name = arrName[random];
		rating = arrRating[random];
		address = arrAddress[random];
		calories = arrCalories[random];
		meal = arrMeal[random];


		if(dUser === "Less than 1 mile") {
			distance = "0.5 mile";
		} else if(dUser === "1-2 miles") {
			distance = "1.3 miles";
		} else if(dUser === "3-5 miles") {
			distance = "4.8 miles";
		} else if(dUser === "6-10 miles") {
			distance = "7.4 miles";
		};


			restaurant.textContent = name;
	        $("#rating").append(rating); 
			$("#address").append(address); 
			$("#cuisine").append(cUser); 
			$("#price").append(pUser);
			$("#distance").append(distance);
			$("#mondayHours").append("9:00AM - 9:00PM");
			$("#tuesdayHours").append("9:00AM - 9:00PM");
			$("#wednesdayHours").append("9:00AM - 9:00PM");
			$("#thursdayHours").append("9:00AM - 9:00PM");
			$("#fridayHours").append("9:00AM - 9:00PM");
			$("#saturdayHours").append("10:00AM - 7:00PM");
			$("#sundayHours").append("11:00AM - 5:00PM");
			$("#calories").append(calories);
			$("#meal").append(meal);

		
	});










// db.users.find_one({"_id": "1"});

	// var MongoClient = require(['mongodb']).MongoClient;
 
// // Connection URL 
//var url = 'mongodb://file:///C:/Users/Lee/Desktop/Restaurants/index.html/hackru_feedme';
// Use connect method to connect to the Server 
// var uri = "mongodb://hackru_feedme:1234@hackru2017feedme-shard-00-00-bsyox.mongodb.net:27017,hackru2017feedme-shard-00-01-bsyox.mongodb.net:27017,hackru2017feedme-shard-00-02-bsyox.mongodb.net:27017/hackru2017feedme?ssl=true&replicaSet=hackru2017feedme-shard-0&authSource=admin"

// // MongoClient.connect("mongodb://hackru_feedme:1234@hackru2017feedme-shard-00-00-wpeiv.mongodb.net:27017,hackru2017feedme-shard-00-01-bsyox.mongodb.net:27017,hackru2017feedme-shard-00-02-bsyox.mongodb.net:27017/<DATABASE>?ssl=true&replicaSet=hackru2017feedme-shard-0&authSource=admin", function(err, db) {
//   MongoClient.connect(uri, function(err, db) {
//   	console.log("Connected");
//   	db.close();
//   });


//   assert.equal(null, err);
//   console.log("Connected correctly to server");
 	
//   insertDocuments(db, function() {
//     updateDocument(db, function() {
//       deleteDocument(db, function() {
//         findDocuments(db, function() {
//           db.close();
//         });
//       });
//     });
//   });
// });

		

// var Db = require('mongodb').Db,
//     MongoClient = require('mongodb').MongoClient,
//     Server = require('mongodb').Server,
//     ReplSetServers = require('mongodb').ReplSetServers,
//     ObjectID = require('mongodb').ObjectID,
//     Binary = require('mongodb').Binary,
//     GridStore = require('mongodb').GridStore,
//     Grid = require('mongodb').Grid,
//     Code = require('mongodb').Code,
//     BSON = require('mongodb').pure().BSON,
//     assert = require('assert');

//   // Set up the connection to the local db
//   var mongoclient = new MongoClient(new Server("localhost", 27017), {native_parser: true});

//   // Open the connection to the server
//   mongoclient.open(function(err, mongoclient) {

//     // Get the first db and do an update document on it
//     var db = mongoclient.db("integration_tests");
//     db.collection('mongoclient_test').update({a:1}, {b:1}, {upsert:true}, function(err, result) {
//       assert.equal(null, err);
//       assert.equal(1, result);

//       // Get another db and do an update document on it
//       var db2 = mongoclient.db("integration_tests2");
//       db2.collection('mongoclient_test').update({a:1}, {b:1}, {upsert:true}, function(err, result) {
//         assert.equal(null, err);
//         assert.equal(1, result);

//         // Close the connection
//         mongoclient.close();
//       });
//     });
//   });