/**
 * Installation:
 * --------------
 * npm init
 * npm install yargs --save
 * npm install firestore-export-import --save
 *
 * Usage:
 * node schedule_update.js [--export | --import]
 * Update schedule_export.js before importing again
 */

 // TODO: Put more effort into yargs
 // TODO: Grab service account from $GOOGLE_APPLICATION_CREDENTIALS

var firestoreService = require("firestore-export-import");
var fs = require('fs');

// Initialize Firebase
var serviceAccount = require("/path/to/service_account.json");
var defaultApp = firestoreService.initializeApp(serviceAccount, "DATABASE_URL_HERE");

// Parse arguments
var argv = require('yargs').argv;
if (argv.export && argv.import) {
  console.log('Please only pass in --export OR --import');
} else if (argv.export) {
  console.log('Exporting BruinFitness schedule to schedule_export.js');
  export_schedule();
} else if (argv.import) {
  console.log('Importing BruinFitness schedule to schedule_export.js');
  firestoreService.restore('schedule_export.json');
} else {
  console.log('Unrecognized argument or no argument passed... \nPlease only pass in --export OR --import');
}

// Export your data
function export_schedule(){
firestoreService
  .backup('schedules')
  .then( function(data) {
    fs.writeFile("schedule_export.json", JSON.stringify(data, null, 4), function(err) {
        if (err) {console.log(err);}
    });
  }
  )
}

