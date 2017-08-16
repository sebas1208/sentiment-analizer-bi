import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';


export interface ITodo {
    text: string,
    state: boolean,
    date: Date
}

@Injectable()
export class TodoService {

    todoArray: Array<ITodo> = [];
    todos: BehaviorSubject<Array<ITodo>> = new BehaviorSubject([]);

    constructor() { }

    addTodo(todo: ITodo) {
        console.log('Add', todo);
        this.todoArray.push(todo);
        this.todos.next(this.todoArray);
    }

    checkTodo(todo: ITodo, index: number) {
        console.log('Check', todo);
        this.todoArray[index] = todo;
        console.log(this.todoArray);
        this.todos.next(this.todoArray);
    }

}
