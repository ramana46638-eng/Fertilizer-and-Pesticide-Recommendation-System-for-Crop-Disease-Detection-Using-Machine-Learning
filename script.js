// ==========================================
// SMART FARMING - MAIN JAVASCRIPT
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    // ==========================================
    // 1. REGISTRATION FORM
    // ==========================================

    const registrationForm =
        document.getElementById("registrationForm");

    if (registrationForm) {

        registrationForm.addEventListener("submit", function (event) {

            const fullname =
                document.getElementById("fullname").value.trim();

            const email =
                document.getElementById("email").value.trim();

            const username =
                document.getElementById("username").value.trim();

            const phone =
                document.getElementById("phone").value.trim();

            const password =
                document.getElementById("password").value;

            const confirmPassword =
                document.getElementById("confirmPassword").value;

            const terms =
                document.getElementById("terms").checked;


            // Check name
            if (fullname === "") {
                event.preventDefault();
                alert("Please enter your full name.");
                return;
            }


            // Check email
            if (email === "") {
                event.preventDefault();
                alert("Please enter your email.");
                return;
            }


            // Check username
            if (username === "") {
                event.preventDefault();
                alert("Please enter a username.");
                return;
            }


            // Check password
            if (password.length < 6) {
                event.preventDefault();
                alert("Password must contain at least 6 characters.");
                return;
            }


            // Check confirm password
            if (password !== confirmPassword) {
                event.preventDefault();
                alert("Password and Confirm Password do not match.");
                return;
            }


            // Check phone
            if (!/^[0-9]{10}$/.test(phone)) {
                event.preventDefault();
                alert("Please enter a valid 10-digit phone number.");
                return;
            }


            // Check terms
            if (!terms) {
                event.preventDefault();
                alert("Please accept the terms and conditions.");
                return;
            }

            /*
             * IMPORTANT:
             * We DO NOT use event.preventDefault()
             * when everything is correct.
             *
             * Therefore the form will be submitted to Flask.
             */

        });

    }


    // ==========================================
    // 2. LOGIN FORM
    // ==========================================

    const loginForm =
        document.getElementById("loginForm");

    if (loginForm) {

        loginForm.addEventListener("submit", function (event) {

            const email =
                document.getElementById("loginEmail").value.trim();

            const password =
                document.getElementById("loginPassword").value;


            if (email === "" || password === "") {

                event.preventDefault();

                alert("Please enter email and password.");

                return;
            }

            /*
             * No preventDefault() here when valid.
             *
             * Flask will receive the login form.
             */

        });

    }


    // ==========================================
    // 3. CROP IMAGE PREVIEW
    // ==========================================

    const cropImage =
        document.getElementById("cropImage");

    const imagePreview =
        document.getElementById("imagePreview");


    if (cropImage && imagePreview) {

        cropImage.addEventListener("change", function () {

            const file = this.files[0];

            if (file) {

                const reader = new FileReader();

                reader.onload = function (event) {

                    imagePreview.src =
                        event.target.result;

                    imagePreview.style.display =
                        "block";

                };

                reader.readAsDataURL(file);

            } else {

                imagePreview.src = "";
                imagePreview.style.display = "none";

            }

        });

    }


    // ==========================================
    // 4. CROP ANALYSIS FORM
    // ==========================================

    const cropForm =
        document.getElementById("cropForm");


    if (cropForm) {

        cropForm.addEventListener("submit", function (event) {

            const crop =
                document.getElementById("crop").value;

            const soil =
                document.getElementById("soil").value;

            const nitrogen =
                document.getElementById("nitrogen").value;

            const phosphorus =
                document.getElementById("phosphorus").value;

            const potassium =
                document.getElementById("potassium").value;

            const temperature =
                document.getElementById("temperature").value;

            const humidity =
                document.getElementById("humidity").value;

            const ph =
                document.getElementById("ph").value;

            const rainfall =
                document.getElementById("rainfall").value;


            // Check crop and soil

            if (crop === "" || soil === "") {

                event.preventDefault();

                alert("Please select crop and soil type.");

                return;
            }


            // Check numerical values

            if (
                nitrogen === "" ||
                phosphorus === "" ||
                potassium === "" ||
                temperature === "" ||
                humidity === "" ||
                ph === "" ||
                rainfall === ""
            ) {

                event.preventDefault();

                alert("Please fill all crop and soil details.");

                return;
            }

            /*
             * IMPORTANT:
             * No preventDefault() when the data is valid.
             *
             * Flask will receive the crop form.
             */

        });

    }


    // ==========================================
    // 5. PROFILE FORM
    // ==========================================

    const profileForm =
        document.getElementById("profileForm");


    if (profileForm) {

        profileForm.addEventListener("submit", function (event) {

            const name =
                document.getElementById("profileName").value.trim();

            const email =
                document.getElementById("profileEmail").value.trim();

            if (name === "" || email === "") {

                event.preventDefault();

                alert("Please fill the required profile information.");

                return;
            }

            /*
             * Flask will handle the profile update.
             */

        });

    }

});