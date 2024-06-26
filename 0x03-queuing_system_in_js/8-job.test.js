import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Create a new Kue queue in test mode
    queue = kue.createQueue({ redis: { prefix: 'test' } });
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit test mode after each test
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 5678 to verify your account' }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Assert that two jobs were created
    expect(queue.testMode.jobs.length).to.equal(2);

    // Assert the details of the first job
    const job1 = queue.testMode.jobs[0];
    expect(job1.type).to.equal('push_notification_code_3');
    expect(job1.data).to.deep.equal(jobs[0]);

    // Assert the details of the second job
    const job2 = queue.testMode.jobs[1];
    expect(job2.type).to.equal('push_notification_code_3');
    expect(job2.data).to.deep.equal(jobs[1]);
  });

  // Add more tests as needed for edge cases, job completion, failure handling, etc.
});
