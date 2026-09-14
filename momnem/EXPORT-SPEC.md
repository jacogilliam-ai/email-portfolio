# Five frames. Five exports. Drop them in this folder.

You are NOT slicing one tall design. Make five separate Figma frames.

Every frame is **1200px wide** with a **cream #FBF5E3 background**, and every one
**ends on cream**. Because they end on cream and the email background is cream,
there is no seam to match. Ignore anything I said earlier about eyedropping hex
values, that only applied to a structure you did not build.

---

## Frame 1 -> `hero.jpg`

Width 1200. Height whatever it lands at, roughly 1150.

Top to bottom:
- The barista photo, cropped, bleeding to both edges
- Logo sitting on the photo
- The maroon box, inset about 60px from each side, overlapping the photo's bottom edge
- Inside the box: THE SUMMER CLASSIC, LATTE ART THROWDOWN, and the two-column
  date / location type. **All of it. Yes, the dates too.**
- About 40px of cream below the box, then the frame ends

Export: **JPG, quality 90**

## Frame 2 -> `pitcher.png`

Width 1200, roughly 560 tall. Cream background.
Pitcher, rosetta, and the smashburgers tag. Cropped tight, no big empty margins.

Export: **PNG**, flattened on cream, no transparency.

## Frame 3 -> `prize.jpg`

Width 1200, roughly 1100 tall.
- The guy holding the machine, cropped from the umbrella down to his waist
- The maroon box inset, overlapping the photo's bottom edge
- Inside it: The Prize / Fellow Series 1
- About 40px of cream below

Export: **JPG, quality 80**

## Frames 4 and 5 -> `product-1.jpg`, `product-2.jpg`

600 x 600 each, square. Just the product shots, no buttons on them.

Export: **JPG, quality 80**

---

# DO NOT export these. They are live HTML already.

- The red "Add it to your calendar" button
- The sentence "Cincy's coffee people go head to head..."
- The FOOD / DRINK / MUSIC row
- WANT TO COMPETE? and THERE'S A SECOND ONE
- Get directions
- "Can't make it? The coffee's still here."
- SHOP NOW buttons (deleted, the product images are the links now)
- SHOP ALL button
- The whole footer

If you export those too you will have them twice.

---

# Then

    cd ~/job-search/portfolio/web
    git add momnem && git commit -m "Add Mom n em throwdown concept" && git push

Live at **jacogilliam-ai.github.io/email-portfolio/momnem/**
Nothing links to it, so it is not published until they say yes.

# Test before you send the link

1. Open it on your phone. Readable, no sideways scroll.
2. Turn images off and reload. You should still see the button, the copy, the
   food/drink/music row, compete, raffle, and the footer. The date and address
   will be gone, which is the tradeoff for keeping them in the designed box.
   That is why `hero.jpg` has the full date and address in its alt text.
3. Click every link. Two `REPLACE_WITH_` placeholders are still in there.

---

# After you replace ANY image

    cd ~/job-search/portfolio/web/momnem
    python3 stamp.py
    cd .. && git add -A momnem && git commit -m "new art" && git push

`stamp.py` rewrites every asset URL with a short hash of that file's bytes.
Filenames stay the same, so your Figma export target does not change, but the
URL changes the instant the image does. Without it a replaced `hero.jpg` keeps
serving the old picture from browser and CDN cache and it looks like nothing
happened.
