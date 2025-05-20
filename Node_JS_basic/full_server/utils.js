import fs from 'fs';

/**
 * Reads a database file and returns student data by field
 * @param {string} path - Path to the CSV file
 * @returns {Promise<Object>} - Promise resolving to an object of arrays
 */
const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n');
    const students = {};

    // Skip header and filter out empty lines
    const fileLines = lines.slice(1).filter((line) => line.trim());

    if (fileLines.length === 0) {
      resolve({});
      return;
    }

    fileLines.forEach((line) => {
      const [firstname, , , field] = line.split(',');

      if (!students[field]) {
        students[field] = [];
      }

      students[field].push(firstname);
    });

    resolve(students);
  });
});

export default readDatabase;
