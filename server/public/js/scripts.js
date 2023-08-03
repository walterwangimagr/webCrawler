document.addEventListener("DOMContentLoaded",async function() {

    async function getPropertyList() {
        const response = await fetch("/allProperties")
        const propertyList = await response.json()
        return propertyList
    }

    async function getPropertyDetailById(id) {
        const response = await fetch(`/getDetail/${id}`)
        const detail = await response.json()
        return detail 
    }

    async function getPropertyImagesById(id) {
        const response = await fetch(`/getImages/${id}`)
        const images = await response.json()
        return images 
    }

    function create_table() {
        var table = document.createElement("table")
        table.classList.add("table")

        var table_template = `
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
            <tbody>
            </tbody>
        `
        table.innerHTML += table_template;
        document.body.appendChild(table)
    }

    async function display_table_content() {
        const tbody = document.querySelector('tbody')
        const property_list = await getPropertyList()

        for (let i = 0; i < property_list.length; i++) {
            const property_id = property_list[i];
            const property_detail = await getPropertyDetailById(property_id)

            const street = property_detail['street'] ? property_detail['street'] : ""
            const img_dir = property_detail['img_dir'] ? property_detail['img_dir'] : ""
            const suburb = property_detail['suburb'] ? property_detail['suburb'] : ""
            const cv = property_detail['cv'] ? property_detail['cv'] : ""
            const land_value = property_detail['land_value'] ? property_detail['land_value'] : ""
            const improvement_value = property_detail['improvement_value'] ? property_detail['improvement_value'] : ""
            const Floor = property_detail['Floor'] ? property_detail['Floor'] : ""
            const Land = property_detail['Land'] ? property_detail['Land'] : ""
            const Beds = property_detail['Beds'] ? property_detail['Beds'] : ""
            const Baths = property_detail['Baths'] ? property_detail['Baths'] : ""
            const sale_method = property_detail['sale_method'] ? property_detail['sale_method'] : ""
            const new_home = property_detail['new_home'] ? property_detail['new_home'] : ""
            const Comments = property_detail['Comments'] ? property_detail['Comments'] : ""

            const new_row = `
                <tr>
                    <td><img id="img_${property_id}" src="${img_dir}"></td>
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
                        <form method="post" action="/sendData/${property_id}">
                        <p>${Comments}</p>
                        <input type="text" name="data">
                        <input type="submit" value="Submit">
                        </form>
                    </td>
                </tr>
            `

            tbody.innerHTML += new_row

            if (i > 10) {
                break
            }
        }
    }

    function imageEventListener(images, id) {
        const img = document.querySelector(`#img_${id}`)
        let currentIndex = 0

        return () => {
            currentIndex = (currentIndex + 1) % images.length
            img.src = `./images/${id}/${images[currentIndex]}`
        }
    }

    async function addAllImageEventListener() {
        const ids = await getPropertyList()
        for (let i = 0; i < ids.length; i++) {
            const id = ids[i]
            const img = document.querySelector(`#img_${id}`)
            const images = await getPropertyImagesById(id)
            img.addEventListener('click', imageEventListener(images, id))
        }
    }
    


    // create_table()
    // await display_table_content()
    // await addAllImageEventListener()
});




