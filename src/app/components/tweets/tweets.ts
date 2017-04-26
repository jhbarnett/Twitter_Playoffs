import { Component, OnInit } from '@angular/core';
import { TweetService } from '../../services/tweetService'

@Component({
  selector: 'tweets',
  template: `<ul>
              <li *ngFor="let tweet of tweets">
                  <div class="userInfo">
                      <a href={{tweet.user_url}}>
                      <img src={{tweet.user_image}}/>
                      <h2>{{tweet.user}}</h2></a>
                  </div>
                  <div class="content">
                      <h4>{{tweet.text}}</h4>
                      <div>{{tweet.created_at}}</div>
                      <div>Retweeted: {{tweet.retweet_count}}</div>
                      <div>Favorited: {{tweet.favorites_count}}</div>
                  </div>
              </li>
            </ul>`,
    styles: [
        'ul {display: flex; flex-direction: row; flex-wrap: wrap; align-items: center; justify-content: space-around; ' +
            'list-style: none; }',
        'li { min-height: calc(90vh/3); width: calc(100vw/4); border: solid 3px #336699; border-radius: 25px;' +
            ' padding: 10px; color: #336699; display: flex; flex-direction: column; margin: 25px 0; }',
        'img { height: 50px; width: auto; border-radius: 50%; }',
        '.userInfo > a { display: flex; justify-content: flex-start; align-items: center; text-decoration: none; ' +
            'text-align: center; color: #336699; }',
        '.userInfo > a > img, .userInfo > a > h2 { max-width: 50%; margin: 15px; }',
        '.content { display: flex; flex-direction: row; flex-wrap: wrap; }'
    ]
})
export class TweetsComponent implements OnInit {
  tweets: Array<{
      user: string,
      user_url: string,
      user_image: string,
      text: string,
      created_at: string,
      retweet_count: number,
      favorites_count: number
  }>;
  error: any;

  constructor(private tweetService: TweetService) { }

  getTweets() {
    this.tweetService
        .getTweets()
        .then(tweets => {
          console.log(tweets)
          return tweets
        })
        .then(tweets => this.tweets = tweets)
        .catch(error => this.error = error);
  }

  ngOnInit() {
    this.getTweets();
  }
}