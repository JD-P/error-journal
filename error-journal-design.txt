XML Scheme for recording classes of software development errors, the process of
fixing them, and their resolution.

<error> - The tag under which the semantic content of each logged error goes. 
	Generally the three types of tag that go under this one are <initial>,
	<update>, <resolution>.

<initial> - Initial writeup of the error, includes a description of the error 
	  (<description>), what the author thinks is probably causing the 
	  problem (<hypothesis>), estimated time to solve the error (<etc>), 
	  the time at which the error was encountered (<time>), what program 
	  the error occurred in (<program>).

<time> - Generic time tag, should be a ISO 8601 combined date and timestamp.
       Represents the date and time of an entry.

<program> - What error the program occured in, only needs to be present in an
	  <initial>.

<description> - What the error is. Only needs to be present in an <initial>.

<hypothesis> - What the author thinks the error is most likely to be. 

<etc> - Estimated Time of Completion. How long the author thinks it will take to
      resolve the issue. Times are given in the format: <time><unit>. Supported
      units are days minutes and seconds. For example: 1d1m1s would be one 
      day one minute and one second from the time of entry.

<update> - An in-progress change in understanding of the error without 
	 resolution. A resolution to the error should go in the <resolved> tag
	 inside the <error> tag. An update always includes a description of what
	 new information has gone into the reevaluation of the error (<new>).
	 It also includes a reestimation of the Estimated Time of Completion 
	 (<etc>). If your etc remains the same 'unchanged' should be written 
	 in on this tag. A new hypothesis may also be stated, again if you do 
	 not have a new hypothesis write in 'unchanged'. The time of the update
	 should be included (<time>).

<resolution> - The final update in understanding of the error, this is the last
	     tag in an <error> tag. It should include a rating from 0-10 of how
	     close the initial hypothesis was to the final cause 
	     (<calibration>). It should also give a description of what solved
	     the problem (<solution>). A description of what actually caused the
	     problem should be included (<cause>). The time of the resolution
	     should be included (<time>).

<cause> - What actually caused a problem once the bug has been fixed and a cause
	is presumably known. If it was the same as your initial hypothesis write
	SAIH (Same As Initial Hypothesis).

<solution> - What solution fixed the problem. 

<calibration> - How close your initial hypothesis was to the final cause from 0
	      to 10. If your hypothesis was dead on give yourself a ten. If
	      your hypothesis indicated the general direction but didn't give
	      an exact fix give yourself a 7. If your hypothesis had no relation
	      to the actual problem give yourself a 0.