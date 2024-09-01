import axios from 'axios';

const submitForm = async (formData) => {
    try {
        const response = await axios.post('/api/submit-form', formData);
        console.log(response.data.message);
    } catch (error) {
        console.error("There was an error submitting the form!", error);
    }
};

const askQuestion = async (question) => {
    try {
        const response = await axios.post('/api/ask-question', { question });
        return response.data.response;
    } catch (error) {
        console.error("There was an error getting the response!", error);
    }
};
