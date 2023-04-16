const puppeteer = require('puppeteer');

(async() =>{
    const browser = await puppeteer.launch({
        headless: false,
        defaultViewport: false,
        userDataDir:"./tmp"
    });
        const page = await browser.newPage();
        await page.goto('https://www.foundit.in/search/freshers-jobs?searchId=efde1b46-0ca0-4334-acbf-965aa2f353c2');
    
    const jobsDetails = await page.$$('.srpLeftSection');

    for(const jobs of jobsDetails){
        
        const title = await page.evaluate(e1 => el.querySelector("div > h3 > a").textContent, jobs)

        console.log(title)
    }

    // await browser.close();
})();