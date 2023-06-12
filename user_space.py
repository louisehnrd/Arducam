<!doctype html>

<html>
    <title>
        Picture
    </title>
    <head>
        <style>
            h1 {
                text-align: center;
            }

            #parameters {
                display: inline-block;
                width: 50%; 
                vertical-align: top; 
                padding-left: 10%;
            }

            #choice {
                display: inline-block;
                width: 50%; 
                vertical-align: top; 
                padding-left: 10%;
            }

            #picture {
                float: right;
                width: 50%;
                margin-top: -35%;
            }

            #last_param {
                float: right;
                width: 50%;
                margin-right: -60%;
            }

            #condition{
                font-size: 60%;
            }

        </style>
        <script>
            // Fonction pour redimensionner une image
            function resizeImage(image, newWidth, newHeight) {
                // Création d'un élément <canvas>
                var canvas = document.createElement('canvas');
                canvas.width = newWidth;
                canvas.height = newHeight;
                
                // Dessin de l'image sur le canvas avec la nouvelle taille
                var context = canvas.getContext('2d');
                context.drawImage(image, 0, 0, newWidth, newHeight);
                
                // Conversion du canvas en une nouvelle image
                var resizedImage = new Image();
                resizedImage.src = canvas.toDataURL('image/jpeg');
                
                // Retourne l'image redimensionnée
                return resizedImage;
            }
              
            // Fonction pour changer automatiquement la photo
            function changerPhotoAutomatiquement() {
                // Création de l'élément <img>
                var image = document.createElement('img');
                
                // Définition de l'attribut src
                image.src = "{{ user_image }}";
                
                // Redimensionnement de l'image à la taille souhaitée (640x480)
                var newWidth = 640;
                var newHeight = 480;
                var resizedImage = resizeImage(image, newWidth, newHeight);
                
                // Suppression de l'ancienne image
                var pictureElement = document.getElementById('picture');
                while (pictureElement.firstChild) {
                    pictureElement.removeChild(pictureElement.firstChild);
                }
                
                // Ajout de la nouvelle image redimensionnée
                pictureElement.appendChild(resizedImage);
            }
            
            // Appel initial de la fonction pour changer la photo
            changerPhotoAutomatiquement();
            
            // Appel de la fonction pour changer la photo toutes les 5 secondes
            setInterval(changerPhotoAutomatiquement, 1000); // Change la photo toutes les 5 secondes (5000 millisecondes)
        </script>
    </head>
    <body>
        <h1>Configuration of the arducam 64mp</h1>
        <div>                
            <div id="parameters">
                <form action="/Param" method="post">
                    <h2>Choose the desired parameters</h2>
                    <p>Enter the width :</p>
                    <p>
                        <input type = "text" name = "width" value="4624"/>                        </p>
                    <p>Enter the height :</p>
                    <p>
                        <input type = "text" name = "height" value="3472"/>
                    </p>
                    <p>Enter zoom factor (1 to 10)</p>
                    <p>
                        <input type = "text" name = "zoom_factor" value="1"/>
                    </p>
                    <p>Enter lens position (0 to 15)*</p>
                    <p>
                        <input type = "text" name = "lens_position" value="None"/>
                    </p>
                    <p id="condition">*If you want autofocus, don't enter anything </p>
                    <p>
                        <input type="submit" name ="parameters" value="submit" />
                    </p>
                </form>
            </div>

            <div id="choice">    
                <form action="/Param" method="post">
                    <h2> Do you want to keep this configuration ? </h2>
                    <select name="reponse">                                    
                        <option value="oui">oui</option>
                        <option value="non">non</option>
                    </select>
                    <input type="submit" name="choice" value="submit">
                </form>
            </div>

            <div id="picture">
            </div>

            <div id="last_param">
                <p> width : {{ width }}, height : {{height}}, zoom : {{zoom_factor}}, lens position : {{lens_position}}</p>
            </div>
        </div>
              
    </body>
</html>
