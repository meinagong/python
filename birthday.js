import prompt from 'prompt';

prompt.start();

const {name_gift_giver} = await prompt.get("What is the name of the gift giver?");
const {present} = await prompt.get("What is the present they gave you?");
const {age} = await prompt.get("How old were you on your birthday?");
const {name} = await prompt.get("What is your name?");

const thanks_card = `Dear ${result.name_gift_giver}, \n\n Thank you for the ${result.present}.\n I really like it. I can't believe\n I am already ${result.age} years old, but\n it does not feel much different than being\n ${result.age-1}.\n\n Sincerely, \n ${result.name}`;

console.log(thanks_card);