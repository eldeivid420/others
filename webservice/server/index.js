// server/index.js

const express = require("express");
var bodyParser = require('body-parser');

const PORT = process.env.PORT || 3001;

const app = express();
const jsonParser = bodyParser.json();
var urlencodedParser = bodyParser.urlencoded({ extended: true });

app.get("/api", (req, res) => {
  res.json({ message: "Hello from server!" });
});


app.post("/fecha", jsonParser, (req, res) => {
  if(!req.body.fecha){
    return res
      .status(500)
      .send("La fecha es un campo obligatorio");
  }

  content = req.body.fecha
  date = new Date(content)
  console.log(date)
  res.json({msg: content})
  
  
});

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});


