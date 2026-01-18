<!DOCTYPE html>
<html lang="en-AU">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LadenPass | Heavy Haulage & Machinery Transport Sydney</title>
    <style>
        /* --- GENERAL STYLES --- */
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
            color: #333;
        }
        a { text-decoration: none; color: inherit; }
        ul { list-style: none; padding: 0; }

        /* --- HEADER --- */
        header {
            background: #1a1a1a;
            color: #fff;
            padding: 1rem 0;
        }
        .container {
            width: 90%;
            max-width: 1200px;
            margin: auto;
            overflow: hidden;
        }
        .logo {
            float: left;
            font-size: 1.5rem;
            font-weight: bold;
            color: #f4b400; /* Safety Yellow */
            display: flex;
            align-items: center;
        }
        .logo img {
            height: 50px; /* Adjust based on your actual logo file */
            margin-right: 10px;
        }
        nav {
            float: right;
            margin-top: 10px;
        }
        nav ul li {
            display: inline;
            margin-left: 20px;
        }
        nav a:hover { color: #f4b400; }

        /* --- HERO SECTION (Background Image) --- */
        #hero {
            /* REPLACE 'heavy-hauler-bg.jpg' with your actual file name */
            background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('heavy-hauler-bg.jpg');
            background-size: cover;
            background-position: center;
            height: 80vh;
            color: #fff;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 0 20px;
        }
        #hero h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            text-transform: uppercase;
        }
        #hero p {
            font-size: 1.2rem;
            margin-bottom: 30px;
        }
        .btn-main {
            background: #f4b400;
            color: #000;
            padding: 12px 30px;
            font-weight: bold;
            border-radius: 5px;
            text-transform: uppercase;
            transition: 0.3s;
        }
        .btn-main:hover { background: #d49b00; }

        /* --- SERVICES SECTION --- */
        #services { padding: 50px 0; text-align: center; }
        .service-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .service-card {
            background: #f4f4f4;
            padding: 20px;
            border-radius: 8px;
            border-bottom: 4px solid #f4b400;
        }

        /* --- QUOTE FORM SECTION --- */
        #quote {
            background: #222;
            color: #fff;
            padding: 50px 0;
        }
        .quote-form input, .quote-form select, .quote-form textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: none;
            border-radius: 4px;
        }
        .form-group { margin-bottom: 10px; }
        .quote-form button {
            width: 100%;
            cursor: pointer;
        }

        /* --- FOOTER --- */
        footer {
            background: #111;
            color: #aaa;
            padding: 20px 0;
            text-align: center;
            font-size: 0.9rem;
        }
        footer p { margin: 5px 0; }
        footer a { color: #f4b400; }

        /* --- MOBILE RESPONSIVENESS --- */
        @media(max-width: 768px) {
            header .container { text-align: center; }
            .logo, nav { float: none; display: block; }
            nav { margin-top: 20px; }
            nav ul li { display: block; margin: 10px 0; }
            #hero h1 { font-size: 2rem; }
        }
    </style>
</head>
<body>

    <header>
        <div class="container">
            <div class="logo">
                <img src="ladenpass-logo.png" alt="LadenPass Logo with Excavator"> 
                LADENPASS
            </div>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#quote">Get a Quote</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section id="hero">
        <h1>Heavy Haulage Specialists</h1>
        <p>Reliable transport for Excavators, Plant & Machinery across Sydney & Regional NSW.</p>
        <a href="#quote" class="btn-main">Get a Free Quote</a>
    </section>

    <section id="services">
        <div class="container">
            <h2>Our Services</h2>
            <p>Based in Padstow, serving the Greater Sydney Area.</p>
            <div class="service-grid">
                <div class="service-card">
                    <h3>Excavator Transport</h3>
                    <p>Safe loading and transport for excavators of all sizes.</p>
                </div>
                <div class="service-card">
                    <h3>Plant Machinery</h3>
                    <p>Bobcats, bulldozers, and heavy industrial equipment.</p>
                </div>
                <div class="service-card">
                    <h3>Regional Haulage</h3>
                    <p>Long-distance transport across New South Wales.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="quote">
        <div class="container">
            <h2 style="text-align: center;">Request a Transport Quote</h2>
            <form class="quote-form" action="https://formspree.io/f/your-form-id" method="POST">
                <input type="text" name="name" placeholder="Your Name" required>
                <input type="email" name="email" placeholder="Your Email" required>
                <input type="tel" name="phone" placeholder="Phone Number" required>
                
                <div style="display: flex; gap: 10px;">
                    <input type="text" name="pickup" placeholder="Pickup Suburb (e.g. Yagoona)" required>
                    <input type="text" name="dropoff" placeholder="Dropoff Suburb" required>
                </div>

                <select name="machinery_type">
                    <option value="" disabled selected>Select Machinery Type</option>
                    <option value="excavator">Excavator</option>
                    <option value="bobcat">Bobcat</option>
                    <option value="vehicle">Vehicle/Car</option>
                    <option value="other">Other Heavy Load</option>
                </select>

                <textarea name="details" rows="4" placeholder="Additional details (Dimensions, Weight, Preferred Date)"></textarea>

                <button type="submit" class="btn-main">Send Request</button>
            </form>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2026 LadenPass Heavy Haulage.</p>
            <p><strong>ABN:</strong> 16 632 316 240</p>
            <p>
                <a href="#">Privacy Policy</a> | 
                <a href="#">Terms of Service</a>
            </p>
        </div>
    </footer>

</body>
</html>
