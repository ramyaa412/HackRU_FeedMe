//Intents

{
  "intents": [
    {
      "intent": "YesIntent"
    },
    {
      "intent": "NoIntent"
    },
    {
      "intent": "EndIntent"
    },
    {
      "intent": "GetCuisineIntent"
    },
    {
      "intent": "RepeatIntent"
    },
    {
      "intent": "ConfirmIntent"
    },
    {
      "intent": "RestaurantIntent"
    },
    {
      "intent": "CustomerIntent"
    },
    {
      "slots": [
        {
          "name": "name",
          "type": "AMAZON.Literal"
        }
      ],
      "intent": "NameIntent"
    },
    {
      "slots": [
        {
          "name": "phonenumber",
          "type": "NUMBER"
        }
      ],
      "intent": "PhonenumberIntent"
    },
    {
      "slots": [
        {
          "name": "choice",
          "type": "AMAZON.FoodEstablishment"
        }
      ],
      "intent": "PickCuisineIntent"
    },
    {
      "slots": [
        {
          "name": "distance",
          "type": "NUMBER"
        }
      ],
      "intent": "DistanceIntent"
    },
    {
      "slots": [
        {
          "name": "price",
          "type": "NUMBER"
        }
      ],
      "intent": "PriceIntent"
    },
    {
      "slots": [
        {
          "name": "time",
          "type": "NUMBER"
        }
      ],
      "intent": "TimeIntent"
    }
  ]
}


//Sample Utterances
YesIntent sure
YesIntent yes
NoIntent no
NoIntent nope
EndIntent thank you
GetCuisineIntent What choices do I have
GetCuisineIntent What is available right now
GetCuisineIntent What restaurants are open
RepeatIntent can you repeat
RepeatIntent go back
ConfirmIntent confirm the order
ConfirmIntent confirm
PickCuisineIntent Can I have {choice}
PickCuisineIntent I want {choice}
DistanceIntent {distance} miles
DistanceIntent within {distance} miles
PriceIntent {price} dollars
PriceIntent within {price} dollars
TimeIntent {time} hours
TimeIntent within {time} hours
NameIntent Please call {name} restaurant
PhoneIntent Please call {number}