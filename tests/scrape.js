const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const fs = require('fs');
const csvWriter = require('csv-write-stream');

// Use the stealth plugin to make Puppeteer more stealthy
puppeteer.use(StealthPlugin());

(async () => {
  // Initialize CSV writer
  let writer = csvWriter({ headers: ["VideoURL", "ThumbnailURL", "H1Content"] });
  writer.pipe(fs.createWriteStream('output.csv'));

  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  // Open the given URL
  await page.goto('https://www.rexporn.sex/videos/search/?query=teen+mega+world', { waitUntil: 'networkidle2' });

  // Find all a tags under the specified div and get their href attributes
  const links = await page.$$eval('div.pitem_screen a', anchors => anchors.map(a => a.href));

  for (let link of links) {
    // Open each link in a new page
    const newPage = await browser.newPage();
    await newPage.goto(link, { waitUntil: 'networkidle2' });

    // Extract the videoURL (assuming it's the src attribute of a video tag)
    const videoUrl = await newPage.$eval('video', video => video.src).catch(() => 'No video found');

    // Extract the thumbnailURL from the link tag
    const thumbnailUrl = await newPage.$eval('link[itemprop="thumbnailUrl"]', link => link.href).catch(() => 'No thumbnail found');

    // Extract the content inside the h1 tag with the specified attribute
    const h1Content = await newPage.$eval('h1[itemprop="name"]', h1 => h1.textContent).catch(() => 'No h1 found');

    // Write the extracted data to the CSV file
    writer.write({ "VideoURL": videoUrl, "ThumbnailURL": thumbnailUrl, "H1Content": h1Content });

    // Close the new page
    await newPage.close();
  }

  // Close the CSV writer
  writer.end();

  // Close the browser
  await browser.close();
})();
