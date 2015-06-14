# Employee Scheduler

An algorithm that schedules people for shifts in a restaurant, the algorithm will change as we start to understand the _Nurse Scheduling Problem_. Currently the scheduler traverses the CSV in a employee-centric way, in other words, it starts with the person and sees what they can do before moving on.

Currently, the algorithm just supports a single shift time, which could be run for multiple times for each shift but that requires 3 separate CSV availability files which is wasteful.

**To Do**
* Prompted Input
* Add multi-shift support for morning, afternoon, graveyard

## Change Log
* CSV -> HTML output conversion
* Data representation changed
    * Increased flexibility & Mathematically Superior for matrix math
