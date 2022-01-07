"""
Test the Timer class. Measure the time it takes from start to end to finish a process
"""

from utils.timer import Timer


def testing_loop(x):
    print('Running a meaningless count from 1 to ' + str(x) + ' to test the Timer class...')

    # Run the meaningless loop to test
    count = 0
    for i in range(1, x):
        count += i

    # Signal completion of loop
    print('Loop completed.')


#######################


def main():
    # Initialize t with Timer class
    t = Timer(12, 45, 476)

    # Testing block 1
    ###############################################
    # Scenario: This test tests the basic base case scenario of timing a loop running 10,000,000
    #   and increment a number by 1 each time.
    # Desired Result: Timer will be displayed in seconds, i.e. timer_config = 1
    # Note: In this test, it is not possible to change the timer config.
    print('Test 1')
    t.start()  # Start the counter
    # Run the testing loop to test Timer functionalities
    # Alternative, paste in your own code to test your own function
    #### Your test function goes here - START ####
    testing_loop(10000000)
    #### Your test function goes here - END ####
    t.end()  # Stop counter and print result
    print()
    ###############################################

    # Testing block 2
    ###############################################
    # Scenario: This test tests the timing of a loop running 20,000,000 times and increment a number by 1 each time.
    # Desired Result: Timer will be displayed in seconds, i.e. timer_config = 1
    # Note: In this test, user can change the timer config.
    print('Test 2')
    t.timerConfig(60)  # Set timer display configuration
    t.start()  # Start the counter
    # Run the testing loop to test Timer functionalities
    # Alternative, paste in your own code to test your own function
    #### Your test function goes here - START ####
    testing_loop(20000000)
    #### Your test function goes here - END ####
    t.end()  # Stop counter and print result
    print()
    ###############################################

    # Testing block 3
    ###############################################
    # Scenario: This test test an exception when the timer configuration is not set in neither hours (3600),
    #   minutes(60) or seconds(1). User is able to configure display time in this test. The testing task is
    #   timing a loop running 30,000,000 times and increment a number by 1 each time.
    # Desired Result:
    #   1. Display a warning message to user that said timer configuration is not implemented and result
    #       will be calculated using default time config, which 1.
    #   2. Timer will be displayed in default time config, which is = 1.
    print('Test 3')
    t.timerConfig(2)  # Set timer display configuration
    t.start()  # Start the counter
    # Run the testing loop to test Timer functionalities
    # Alternative, paste in your own code to test your own function
    #### Your test function goes here - START ####
    testing_loop(30000000)
    #### Your test function goes here - END ####
    t.end()  # Stop counter and print result
    print()
    ###############################################

    # Testing block 4
    ###############################################
    # Scenario: This test demonstrates the functionality that enables user to change time config and retrieve
    #   the last timer result
    # Desired Result:
    #   1. User can call timerConfig with different argument value to set the time config. The only available value
    #       is: hours (3600), minutes(60) or seconds(1). If the timer config value is not in this selection,
    #       display a warning message and display the result by default in seconds.
    #   2. Display the last timer result.
    #### Your test function goes here - START ####
    print('Test 4')
    t.timerConfig(3600)  # Set timer display configuration
    t.retrieveLastResult()  # Retrieve and print last timer result
    #### Your test function goes here - END ####
    print()



if __name__ == '__main__':
    main()