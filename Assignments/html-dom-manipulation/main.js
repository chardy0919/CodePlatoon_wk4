const replaceImages = (event) => {
    // event.preventDefault()
    let images = document.body.getElementsByTagName("img")
    let newAlt = document.createTextNode("This is no longer an image.")
    
    for (let i=0;i<images.length;i++) {
        let parent = images[i].parentNode;
        console.log(parent)
        parent.replaceChild(newAlt,images[i])
 }
    
}