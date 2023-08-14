import React, {useState} from 'react';
import MyInput from "./UI/input/MyInput";
import MyButton from "./UI/button/MyButton";

const EventForm = ({create}) => {
    const [task, setEvent] = useState({title: '', duration: '', description: ''})


    const addNewEvent = (e) => {
        e.preventDefault()
        const newEvent = {
            ...task, id: Date.now()
        }
        create(newEvent)
        setEvent({title: '', duration: '', description: ''})
    }

    return (
        <form>
            {/*Управляемый компонент*/}
            <MyInput
                value={_event.title}
                onChange={e => setPost({...task, title: e.target.value})}
                type="text"
                placeholder="Название мероприятия"
            />
            {/*Неуправляемый\Неконтролируемый компонент*/}
            <MyInput
                value={_event.duration}
                onChange={e => setPost({...task, duration: e.target.value})}
                type="number"
                placeholder="Описание продолжительность мероприятия"
            />
            <MyInput
                value={_event.description}
                onChange={e => setPost({...task, description: e.target.value})}
                type="text"
                placeholder="Описание мероприятия"
            />
            <MyButton onClick={addNewEvent}>Создать мероприятие</MyButton>
        </form>
    );
};

export default PostForm;