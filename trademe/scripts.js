document.addEventListener("DOMContentLoaded",async function() {

    async function loadJSON() {
        try {
            const response = await fetch('database.json');
            const database = await response.json();
            return database
        } catch (error) {
            console.error(error);
            return ""
        }
    }

    function add_table_header(table) {
        var header_template = `
            <thead>
                <tr>
                    <th>Image</th>
                    <th>Address</th>
                    <th>CV</th>
                    <th>Land value</th>
                    <th>Inprovement value</th>
                    <th>Floor</th>
                    <th>Land</th>
                    <th>Beds</th>
                    <th>Baths</th>
                    <th>Sale Method</th>
                    <th>New House</th>
                    <th>Comments</th>
                </tr>
            </thead>
        `
        table.innerHTML += header_template;
        return table
    }

    
    async function add_table_body(data, table) {
        // read databse 
        
        var tbody = document.createElement("tbody")
        for (const id in data) {
            const property_detail = data[id]
            var img_dir = "img_dir" in property_detail ? property_detail['img_dir'] : ""
            var sale_method = "sale_method" in property_detail ? property_detail['sale_method'] : ""
            var new_home = "new_home" in property_detail ? property_detail['new_home'] : ""
            var Beds = "Beds" in property_detail ? property_detail['Beds'] : ""
            var Baths = "Baths" in property_detail ? property_detail['Baths'] : ""
            var Land = "Land" in property_detail ? property_detail['Land'] : ""
            var street = "street" in property_detail ? property_detail['street'] : ""
            var suburb = "suburb" in property_detail ? property_detail['suburb'] : ""
            var cv = "cv" in property_detail ? property_detail['cv'] : ""
            var land_value = "land_value" in property_detail ? property_detail['land_value'] : ""
            var improvement_value = "improvement_value" in property_detail ? property_detail['improvement_value'] : ""
            var Floor = "Floor" in property_detail ? property_detail['Floor'] : ""
            var Comments = "Comments" in property_detail ? property_detail['Comments'] : ""

            const new_row = `
                <tr>
                    <td><img id="${id}" src="${img_dir}"></td>
                    <td>${street}, ${suburb}</td>
                    <td>${cv}</td>
                    <td>${land_value}</td>
                    <td>${improvement_value}</td>
                    <td>${Floor}</td>
                    <td>${Land}</td>
                    <td>${Beds}</td>
                    <td>${Baths}</td>
                    <td>${sale_method}</td>
                    <td>${new_home}</td>
                    <td>
                        <p>${Comments}</p>
                        <p>test</p>
                        <input id="text_${id}" type="text">
                        <button id="button_${id}">save</button>
                    </td>
                </tr>
            `
            tbody.innerHTML += new_row
        }
        table.appendChild(tbody)
        return table
    }

    async function getImageById(id) {
        const folderUrl = "./images/" + id
        try {
            const response = await fetch(folderUrl);
            const data = await response.text();
            const parser = new DOMParser();
            const htmlDoc = parser.parseFromString(data, 'text/html');
            const links = htmlDoc.getElementsByTagName('a');
            const filenames = Array.from(links)
            .filter(link => !link.href.endsWith('/') && link.href.endsWith('.jpg')) // exclude subfolders
            .map(link => link.href);
            return filenames; // return array of filenames
        } catch (error) {
            console.error(error);
        }
    }

    var currentIndex = 0;
    function showImage(img, images) {
        img.src = images[currentIndex];
        currentIndex = (currentIndex + 1) % images.length;
    }

    async function add_click_eventListeners(id) {
        const images = await getImageById(id)
        const img = document.getElementById(id)
        img.addEventListener("click", function () {
            showImage(img, images)
        })
    }

    async function add_button_eventListeners(id) {
        const button = document.getElementById(`button_${id}`)
        const input = document.getElementById(`text_${id}`)
        button.addEventListener("click", async () => {
            const text = input.value 
            const data = await loadJSON()
            const 
            console.log(data)
        })
    }

    async function create_table(data) {
        var table = document.createElement("table")
        table.classList.add("table")
        table = add_table_header(table)
        table = await add_table_body(data, table)
        document.body.appendChild(table)
        for (const key in data) {
            await add_click_eventListeners(key)
            add_button_eventListeners(key)
        }
    }



    const data = await loadJSON()
    await create_table(data)
});




