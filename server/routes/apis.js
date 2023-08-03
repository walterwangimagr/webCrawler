const express = require("express")
const fs = require('fs')
const router = express.Router()

function createArray(n) {
    const arr = []
    for (let i = 1; i < n+1; i++) {
        arr.push(i)
    }
    return arr
}


router.get("/", async (req, res) => {
    const path = './public/database/database.json'
    const file = fs.readFileSync(path, 'utf8')
    const database = JSON.parse(file)
    const ids = Object.keys(database)
    const num_property = Math.ceil(ids.length / 10)  
    res.locals.indexs = createArray(num_property)

    //first 10 ids
    const firstTen = Object.entries(database).slice(0, 10)
    res.locals.data = firstTen
    console.log(firstTen)
    res.render("index")

})

router.get("/getImages/:propertyId", async function (req, res) {
    const id = req.params['propertyId']
    const dir_path = `./public/images/${id}`
    const imgs = await fs.promises.readdir(dir_path)
    res.send(imgs)
})

router.get("/getDetail/:propertyId", async function (req, res) {
    const id = req.params['propertyId']
    const path = './public/database/database.json'
    const file = fs.readFileSync(path, 'utf8')
    const data = JSON.parse(file)
    res.send(data[id])
})

router.get("/allProperties", async function (req, res) {
    const path = './public/database/database.json'
    const file = fs.readFileSync(path, 'utf8')
    const data = JSON.parse(file)
    const ids = Object.keys(data)
    res.send(ids)
})

router.post("/sendData/:propertyId", async function (req, res) {
    const id = req.params['propertyId']
    const Comments = req.body.data
    console.log(Comments)
    console.log(id)

    await fs.readFile('public/database/database.json', (err, data) => {
        if (err) throw err;
        
        // Parse the JSON data into a JavaScript object
        const database = JSON.parse(data);
        
        // Update the object with new data
        database[id].Comments = Comments
        
        // Write the updated object back to the JSON file
        fs.writeFile('public/database/database.json', JSON.stringify(database), (err) => {
            if (err) throw err;
            console.log('Data updated successfully');
        });
    });

    res.redirect("/")
})


module.exports = router