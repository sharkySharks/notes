# React with Redux

- React is a JS library that produces HTML components (the view)
    + only one component per file
    + `react-dom` is the library that renders components to the DOM
    + JSX is Javascript XML syntax that looks like HTML and makes writing React components easier
    ```
    // index.js
    import React from 'react';
    import ReactDOM from 'react-dom';
    import SearchBar from './components/searchbar';

    const App = () => {
        return (
            <div>
                <SearchBar />
            </div>
        ); // JSX
    }
    // <App /> creates an instance of the App class above, it can be self-closing if there are no subcomponents
    // then you have to give it a base DOM node
    ReactDOM.render(<App />, document.querySelector('.container'));
    ```
    + functional components vs class components
        * functional components are simpler components that do not need to be aware of themselves or state, ie dumb component
            - `props` come through the parameter of the fn, `props`
        * class component can introspect itself, use when you need to be aware of state
            - `props` are available anywhere in the component as `this.props`
    + State
        * every class-based component has its own state object (not fn components)
        * every time the state changes the component re-renders
        * only set state in the constructor, otherwise manipulate state with `this.setState()` method
    ```
    // components/searchbar.js
    import React, { Component } from 'react'; // need this for JSX

    class SearchBar extends Component {
        constructor(props) {
            super(props);

            this.state = { term: ''};
        }
        
        // every class component needs a render fn
        // receives its value from state
        render() {
            return (
                <div>
                    <input 
                        value={this.state.term}
                        onChange={event => this.setState({ term: event.target.value })} />;
                </div>
            );
        }
    }

    export default SearchBar;
    ```
    + JSX components use `className` instead of `class` in JSX to avoid naming collisions
    + Data
        * Top-most component using the data should get the data from the API
        * pass data from one component to another via `props` object and adding properties to the components
            - `this.props` in class-based components, `props` parameter in functional components
            - parent/child component data passing
            - don't really want to do this more than 2-3 levels deep
    ```
    // videoList.js
    import React from 'react';
    import VideoListItem from './videoListItem';

    const VideoList = (props) => {
        const videoItems = props.videos.map((video) => {
            return <VideoListItem key={video.etag} video={video} />
        });
        return (
            <ul className="col-md-4 list-group">
                {videoItems}
            </ul>
        );
    };
    export default VideoList;

    // videoListItem.js
    import React from 'react';
    
    // `{video}` is shorthand for assigning `props.video` to `video` (ES6)
    const VideoListItem = ({video}) => {
        return <li>Video</li>
    };
    export default VideoListItem;
    ```

- Redux
    + Predictable state container for React applications
    + Separates data from the view layer
        * think about the difference between what data you need and what the views are displaying
    + React is the views, Redux is the data
    + All the data is centralized in one global object
    + Counter Example (buttons add and subtract from the counter):
        * Redux - stores the current count
        * React - displays the current count and executes the number changer functionality





