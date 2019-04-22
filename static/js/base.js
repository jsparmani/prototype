
function check_url() {
    url = window.location.href
    scrollPixel = $('html').scrollTop()
    window.localStorage.setItem("url", url)
    window.localStorage.setItem("scrollPixel", scrollPixel)
}

function manage() {
    if (window.location.href.includes('search')) {
        document.scrollingElement.scrollTop += parseFloat(localStorage.getItem("scrollPixel"))

    }
    

    if (window.location.href.includes('list_applicant')) {
        document.scrollingElement.scrollTop += parseFloat(localStorage.getItem("scrollPixel"))

    }

    if (window.location.href.includes('edit_transactions_admin')) {
        document.scrollingElement.scrollTop += parseFloat(localStorage.getItem("scrollPixel"))

    }

    if (window.location.href.includes('check_url')) {

        window.location.href = localStorage.getItem("url");
    }
}


