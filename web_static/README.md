# Web Static: Airbnb Clone - HTML & CSS

## Overview

This project is a static version of Airbnb, focusing on replicating the layout and styling using HTML and CSS.

## Technologies Used

- HTML5
- CSS3

## HTML Elements and Tags

### Header

```html
<header>
    <h1>Web Static: Airbnb Clone</h1>
    <!-- Navigation links, search bar, user profile, etc. -->
</header>
```

### Filters Box

```html
<aside class="filters-box">
    <!-- Filter options (e.g., location, price, amenities) -->
    <button class="search-button">Search</button>
</aside>
```

### Main Section

```html
<main>
    <!-- Featured listings, search results, filters, etc. -->
</main>
```

### Footer

```html
<footer>
    <!-- Footer links, contact information, social media links, etc. -->
</footer>
```

## CSS Selectors and Properties

### Styling Header

```css
header {
    background-color: #ff5a5f;
    color: white;
    padding: 10px;
    text-align: center;
    /* Add more styles as needed */
}
```

### Styling Filters Box

```css
.filters-box {
    background-color: #f4f4f4;
    padding: 15px;
    /* Add more styles as needed */
}

.search-button {
    background-color: #ff5a5f;
    color: white;
    padding: 10px;
    cursor: pointer;
    /* Add more styles as needed */
}
```

### Styling Listings

```css
main {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    /* Add more styles as needed */
}
```

### Styling Footer

```css
footer {
    background-color: #333;
    color: white;
    padding: 20px;
    text-align: center;
    /* Add more styles as needed */
}
```

## Examples

### Adding a New Listing

```html
<main>
    <div class="listing">
        <img src="listing-image.jpg" alt="Listing Image">
        <h2>Cozy Apartment in the City Center</h2>
        <p>Price: $100/night</p>
        <!-- Additional details and booking button -->
    </div>
    <!-- Add more listings as needed -->
</main>
```

### Styling User Profile

```css
header .user-profile {
    border: 2px solid #fff;
    border-radius: 50%;
    margin-left: auto;
}
```

## CSS Files

- `header.css`
- `filters.css`
- `footer.css`

## Running the Project

1. Clone the repository.
2. Open `index.html` in a web browser.

