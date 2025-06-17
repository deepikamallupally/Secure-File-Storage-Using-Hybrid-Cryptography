Objective:
To provide a secure platform for storing files on the cloud using hybrid cryptography.

Methodology:
To achieve the above goal, the following methodology needs to be followed:

1.Load the File on the Server

2.Upload the file to the server where it will be processed.

3.Divide the Uploaded File into N Parts

4.Split the uploaded file into N smaller parts for better security and manageability.

5.Encrypt All Parts of the File

6.Encrypt each part using a selected cryptographic algorithm.

7.Algorithms are changed with every part in a round-robin fashion to enhance security.

8.Secure the Keys for Cryptographic Algorithms

9.The keys used for encrypting the parts are secured using a different cryptographic algorithm.

10.The key for this secondary algorithm is provided to the user as a public key.

After completing these steps, you will have N encrypted files stored on the server and a public key available for download, which will be used for decrypting the files.

Restoring the File:
1.To restore the original file, follow these steps:

2.Load the Key on the Server

3.Upload the public key to the server.

4.Decrypt the Keys for the Algorithms

5.Decrypt the keys for the primary cryptographic algorithms using the uploaded public key.

6.Decrypt All Parts of the File

7.Decrypt each of the N parts using the previously decrypted keys and the same algorithms used during encryption.

8.Combine All Parts to Form the Original File

9.Merge all the decrypted parts to reconstruct the original file.

10Provide the reconstructed file for the user to download.

How to Run
Note: This project is based on Python latest version. Running it on any other platform might create compatibility issues.

Steps:
Install Requirements

bash
pip install -r requirements.txt
Run the Application

bash
python app.py
Visit the Localhost

Open your web browser and navigate to http://localhost:8000 to access the application.

Enjoy!

Follow the application instructions to upload, encrypt, decrypt, and download your files securely.

Contact Information
If you encounter any bugs or have suggestions for improving the project, feel free to contact:

Deepika Mallupally

LinkedIn: https://www.linkedin.com/in/deepika-mallupally-5a52b5282/

Note: The project has encountered a bug due to updates in the cryptography library. If you are interested in collaborating to improve this project, feel free to reach out via the LinkedIn link above.
