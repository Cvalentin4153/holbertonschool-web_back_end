import readDatabase from '../utils';

/**
 * Students controller for managing student routes
 */
class StudentsController {
  /**
   * Get all students route handler
   * @param {Object} request - Express request object
   * @param {Object} response - Express response object
   */
  static getAllStudents(request, response) {
    // Get database path from command line arguments
    const path = process.argv[2];

    readDatabase(path)
      .then((data) => {
        const responseLines = ['This is the list of our students'];

        // Sort fields alphabetically case insensitive
        const sortedFields = Object.keys(data).sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));

        sortedFields.forEach((field) => {
          const students = data[field];
          responseLines.push(
            `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`,
          );
        });

        response.status(200).send(responseLines.join('\n'));
      })
      .catch((error) => {
        response.status(500).send(error.message);
      });
  }

  /**
   * Get all students by major route handler
   * @param {Object} request - Express request object
   * @param {Object} response - Express response object
   */
  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    // Validate major parameter
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    // Get database path from command line arguments
    const path = process.argv[2];

    readDatabase(path)
      .then((data) => {
        const students = data[major] || [];
        response.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch((error) => {
        response.status(500).send(error.message);
      });
  }
}

export default StudentsController;
