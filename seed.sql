INSERT INTO role (role_name) VALUES ('administrator'), ('general user');


INSERT INTO "user" (username, email, password, role_id, date_added) VALUES ('Zeus', 'god_of_lightning@fake_email.com', 'scrypt:32768:8:1$P3fn40PccjmNfnqn$61efb1616bceebef1f1a6ab2fa17adb0371b137ff6032ba37d78f43989cdffa97a2e905d5330650cdee00061d6583d48205289825d4ddd2687038992ce6f5612', 1, now());
