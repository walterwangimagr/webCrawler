const express = require('express')
const app = express()
const port = 8888

const engine = require("express-handlebars")
app.engine('handlebars', engine({
    defaultLayout: false
}));
app.set('view engine', 'handlebars');
app.set('views', './views');


const path = require("path")
app.use(express.static(path.join(__dirname, "public")))


const bodyParser = require("body-parser")
app.use(bodyParser.urlencoded({ extended: false }))



const apis = require("./routes/apis.js")
app.use(apis)
app.listen(port, () => console.log(`Example app listening on port ${port}!`))