import { Component } from '@angular/core';
import { TweetsComponent } from './components/tweets/tweets'
import { TweetService } from './services/tweetService'

@Component({
  selector: 'my-app',
  template: `<h1>Hello {{name}}<span *ngIf="itIsJuly">, DjangoCon</span>!</h1>
              <tweets></tweets>`,
  directives: [TweetsComponent],
  providers: [TweetService]
})

export class AppComponent {
  name:string = 'World'
  itIsJuly:boolean

  constructor() {
      var date = new Date()
      this.itIsJuly = (date.getMonth() == 6 && date.getFullYear() == 2016)
  }
}
