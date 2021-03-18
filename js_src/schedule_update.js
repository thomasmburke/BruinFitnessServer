/**
 * Installation:
 * --------------
 * npm init
 * npm install yargs --save
 * npm install firestore-export-import --save
 *
 * Usage:
 * node schedule_update.js [--export | --import]
 * Update schedule_export.json before importing again
 */

 // TODO: Put more effort into yargs

const { initializeApp, restore, backup } = require('firestore-export-import')
var fs = require('fs');

// Initialize Firebase
var serviceAccount = require("../creds/bruinfitnessprod-firebase-adminsdk.json");
initializeApp(serviceAccount);

// Parse arguments
var argv = require('yargs').argv;
if (argv.export && argv.import) {
  console.log('Please only pass in --export OR --import');
} else if (argv.export) {
  console.log('Exporting BruinFitness schedule to schedule_export.js');
  export_schedule();
} else if (argv.import) {
  console.log('Importing BruinFitness schedule to schedule_export.js');
  restore('./importFiles/schedule_export.json');
} else {
  console.log('Unrecognized argument or no argument passed... \nPlease only pass in --export OR --import');
}

// Export your data
function export_schedule(){
// backup('schedules/San Leandro/schedule')
backup(`schedules/Redwood City/dates/2021-01-15/classes`)
  .then( function(data) {
    fs.writeFile("./importFiles/schedule_export.json", JSON.stringify(data, null, 4), function(err) {
        if (err) {console.log(err);}
    });
  }
  )
}

