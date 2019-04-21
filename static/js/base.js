
function check_url() {
    url = window.location.href
    scrollPixel = $('html').scrollTop()
    window.localStorage.setItem("url", url)
    window.localStorage.setItem("scrollPixel", scrollPixel)
}

function manage() {
    // console.log('Hi');
    if (window.location.href.includes('search')) {
        document.scrollingElement.scrollTop += parseFloat(localStorage.getItem("scrollPixel"))
        
    }
    if (window.location.href.includes('check_url')) {
        // console.log("Hello");
        window.location.href = localStorage.getItem("url");

        // $('html').scrollTop += localStorage.getItem("scrollPixel");
    }
}
