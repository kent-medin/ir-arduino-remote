//------------------------------------------------------------------------------
// Include the IRremote library header
//
#include <IRremote.h>

//------------------------------------------------------------------------------
// Tell IRremote which Arduino pin is connected to the IR Receiver (TSOP4838)
//
int recvPin = 5;
IRrecv irrecv(recvPin);

//+=============================================================================
// Configure the Arduino
//
void setup()
{
  Serial.begin(115200); // Status message will be sent to PC at 9600 baud
  irrecv.enableIRIn();  // Start the receiver
}

// Dump out the decode_results structure.
//
void dumpData(decode_results *results)
{
  Serial.print(results->value, HEX);
  Serial.print("\n");
  Serial.flush();
}

//+=============================================================================
// The repeating section of the code
//
void loop()
{
  decode_results results; // Somewhere to store the results

  if (irrecv.decode(&results))
  {
    dumpData(&results);
    irrecv.resume();
  }
}
