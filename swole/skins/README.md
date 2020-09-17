# Skins

`Skins` are how your page look like. It allow you to customized the look of your page really easily.

A `Skin` is a simple CSS file, containing rule for your page's HTML.

## List of existing Skins

Currently, only the `base` skin is available in `swole`. It's the default skin, you have nothing to do to use it.

## Create your own Skin

To create your custom Skin, simply copy the file `base.css`, which act as a template. You can then add or remove CSS rules to customize the look of your page.

If you need to import external CSS library, write it as a comment on top of your file. You can import several libraries.

Similarly, you can add fonts. Just separate it from the external library with an additional new line, and write a comment with the link to the font.

In the end, your file might look like :

```css
/* https://external/library/1.css */
/* https://external/library/2.css */

/* https://external/font/1 */
/* https://external/font/2 */
/* https://external/font/3 */

body {
    font-size: 1rem;
}
```

