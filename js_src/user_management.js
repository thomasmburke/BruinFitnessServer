var admin = require('firebase-admin');

// Run the following command to set the env var for firebase
// export GOOGLE_APPLICATION_CREDENTIALS="/Users/tomburke/Desktop/repos/BruinFitnessServer/creds/bruinfitnessprod-firebase-adminsdk.json"

var app = admin.initializeApp();

let uid = "hkynE2ZsgrahlI57GsNKBg0ULdz1"

// admin
//   .auth()
//   .getUser(uid)
//   .then((userRecord) => {
//     // See the UserRecord reference doc for the contents of userRecord.
//     console.log(`Successfully fetched user data: ${JSON.stringify(userRecord, null, 2)}`);
//   })
//   .catch((error) => {
//     console.log('Error fetching user data:', error);
//   }).then(() => admin.app().delete());

  // admin
  // .auth()
  // .setCustomUserClaims(uid, { admin: true })
  // .then(() => {
  //   // The new custom claims will propagate to the user's ID token the
  //   // next time a new one is issued.
  //   console.log(`custom claims added for ${uid}`);
  //   // admin.app().delete();
  // });


  admin
  .auth()
  .createUser({
    email: 'jesusmendez@foobar.com',
    emailVerified: false,
    password: 'supersecret',
    displayName: 'Jesus Mendez',
    disabled: false,
  })
  .then((userRecord) => {
    // See the UserRecord reference doc for the contents of userRecord.
    console.log('Successfully created new user:', userRecord.uid);
  })
  .catch((error) => {
    console.log('Error creating new user:', error);
  }).then(() => admin.app().delete());
