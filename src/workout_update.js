/**
 *
 * Usage:
 * node workout_update.js [--export | --import]
 * Update workout_{date}_export.json before importing again
 */

 // TODO: Put more effort into yargs

 const { initializeApp, restore, backup } = require('firestore-export-import')
 var fs = require('fs');
 
 // Initialize Firebase
 var serviceAccount = require("../creds/bruinfitnessprod-firebase-adminsdk.json");
 initializeApp(serviceAccount);

 const getTodaysFirestoreDateString = () => {
    let today = new Date();
    let day = String(today.getDate());
    let month = String(today.getMonth() + 1); //January is 0!
    let year = String(today.getFullYear());
    return `${year}_${month}_${day}`;
    }

 
 // Parse arguments
 var argv = require('yargs').argv;
 if (argv.export && argv.import) {
   console.log('Please only pass in --export OR --import');
 } else if (argv.export) {
   console.log(`Exporting BruinFitness workout to importFiles/workout_${getTodaysFirestoreDateString()}_export.json`);
   export_workout();
 } else if (argv.import) {
   console.log(`Importing BruinFitness workout to workout_${getTodaysFirestoreDateString()}_export.js`);
   restore(`./importFiles/workout_${getTodaysFirestoreDateString()}_export.json`);
 } else {
   console.log('Unrecognized argument or no argument passed... \nPlease only pass in --export OR --import');
 }
 
 // Export your data
 function export_workout(){
 backup('workouts/2020_02_14')
   .then( function(data) {
     fs.writeFile(`./importFiles/workout_${getTodaysFirestoreDateString()}_export.json`, JSON.stringify(data, null, 4), function(err) {
         if (err) {console.log(err);}
     });
   }
   )
 }

